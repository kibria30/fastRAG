from langchain_groq import ChatGroq

from app.config import settings
from app.services.llm_services.baseLLMService import BaseLLMService


class GroqLLMService(BaseLLMService):
    def _default_llm(self):
        return ChatGroq(
            model=settings.GROQ_MODEL,
            api_key=settings.GROQ_API_KEY,
            temperature=0.2,
        )
