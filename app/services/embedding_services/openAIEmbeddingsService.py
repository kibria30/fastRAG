from langchain_openai import OpenAIEmbeddings
from app.config import settings
from app.services.embedding_services.baseEmbeddingsService import BaseEmbeddingsService

class OpenAIEmbeddingsService(BaseEmbeddingsService):
    def __init__(self, embedding_model=None):
        if embedding_model is None:
            embedding_model = OpenAIEmbeddings(
                model=settings.OPENAI_EMBEDDING_MODEL,
                api_key=settings.OPENAI_API_KEY,
            )
        super().__init__(embedding_model)

    def embed(self, text):
        return self.embedding_model.embed_query(text)
