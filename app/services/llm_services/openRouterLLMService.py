from langchain_openrouter import ChatOpenRouter
from app.config import settings
from app.services.llm_services.baseLLMService import BaseLLMService


class OpenRouterLLMService(BaseLLMService):

    def _default_llm(self) -> ChatOpenRouter:
        primary = ChatOpenRouter(
            model=settings.OPENROUTER_PRIMARY_MODEL,
            api_key=settings.OPENROUTER_API_KEY,
            temperature=0.2,
        )
        backup_model = ChatOpenRouter(
            model=settings.OPENROUTER_FALLBACK_MODEL,
            api_key=settings.OPENROUTER_API_KEY,
            temperature=0.2,
        )
        return primary.with_fallbacks([backup_model])