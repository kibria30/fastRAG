from app.services.embedding_services.baseEmbeddingsService import BaseEmbeddingsService
from fastembed import TextEmbedding

class LocalEmbeddingsService(BaseEmbeddingsService):
    def __init__(self, embedding_model=None):
        if embedding_model is None:
            embedding_model = TextEmbedding() # model_name="BAAI/bge-small-en-v1.5"  -> default model
        super().__init__(embedding_model)

    def embed(self, texts):
        return list(self.embedding_model.embed(texts))
