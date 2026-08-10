class BaseEmbeddingsService:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def embed(self, text):
        raise NotImplementedError("Subclasses should implement this method.")