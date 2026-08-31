from abc import ABC, abstractmethod
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.language_models.chat_models import BaseChatModel
from app.services.tool_services import TOOLS
from app.domains import DOMAINS, DEFAULT_DOMAIN


TOOL_MAP = {tool.name: tool for tool in TOOLS}

class BaseLLMService(ABC):
    def __init__(self, llm: BaseChatModel = None):
        self.llm = llm or self._default_llm()
        self.llm_with_tools = self.llm.bind_tools(TOOLS) if TOOLS else self.llm


    @abstractmethod
    def _default_llm(self) -> BaseChatModel:
        raise NotImplementedError("Subclasses should implement this method.")


    def build_context_block(self, chunks: list[dict]) -> str:
        parts = []
        for i, chunk in enumerate(chunks, start=1):
            parts.append(f"[{i}] (source: {chunk['source']})\n{chunk['text']}")
        return "\n\n".join(parts)


    async def generate_answer(self, query: str, chunks: list[dict], domain: str = DEFAULT_DOMAIN) -> dict:
        context_block = (
            self.build_context_block(chunks) if chunks
            else "(no relevant documents found in the knowledge base)"
        )
        user_prompt = (
            f"Context:\n{context_block}\n\n"
            f"Question: {query}\n\n"
            f"Answer using only the context above."
        )

        system_prompt = DOMAINS[domain]["system_prompt"]
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        response = await self.llm_with_tools.ainvoke(messages)

        if not response.tool_calls:
            return {
                "content": response.content,
                "tools_used": []
            }

        messages.append(response)

        for call in response.tool_calls:
            tool = TOOL_MAP.get(call["name"])
            if tool is None:
                result = {"error": f"Unknown tool: {call['name']}"}
            else:
                try:
                    result = await tool.ainvoke(call["args"])
                except Exception as exc:
                    result = {"error": str(exc)}

            messages.append(
                ToolMessage(content=str(result), tool_call_id=call["id"])
            )

        final_response = await self.llm_with_tools.ainvoke(messages)

        return {
            "content": final_response.content,
            "tools_used": [tool["name"] for tool in response.tool_calls]
        }