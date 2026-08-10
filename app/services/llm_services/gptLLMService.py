from langchain_openai import ChatOpenAI
from app.config import settings
from app.services.llm_services.baseLLMService import BaseLLMService


class GPTLLMService(BaseLLMService):

    def _default_llm(self) -> ChatOpenAI:
        return ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key=settings.OPENAI_API_KEY,
            temperature=0.2,
        )
