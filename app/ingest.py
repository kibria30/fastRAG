from app.services.embedding_services.localEmbeddingsService import LocalEmbeddingsService
from app.services.vector_store_service import QdrantStore
from app.services.chunking import chunk_folder
from app.config import settings


def run(docs_folder: str, collection_name: str):
    embedder = LocalEmbeddingsService()
    store = QdrantStore(collection_name=collection_name)

    vector_size = len(embedder.embed("Vector Size Test")[0])

    store.ensure_collection(vector_size=vector_size)

    all_chunks = chunk_folder(docs_folder)
    vectors = embedder.embed([chunk["text"] for chunk in all_chunks])
    store.upsert_chunks(all_chunks, vectors)


if __name__ == "__main__":
    run(settings.FARMING_KNOWLEDGE_BASE_PATH, settings.FARMING_KNOWLEDGE_BASE_COLLECTION_NAME)