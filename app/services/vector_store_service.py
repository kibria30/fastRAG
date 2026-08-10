import uuid

from qdrant_client import QdrantClient
from app.config import settings
from qdrant_client.http import models as qmodels


def _chunk_id(chunk: dict) -> str:
    """
    Deterministic ID derived from source file + text content.
 
    uuid.uuid5 (unlike uuid4) always produces the SAME output for the same
    input string. So the same chunk, re-ingested after you edit potato.md
    and re-run ingest.py, gets the same id and overwrites its old vector/
    payload in place instead of creating a duplicate point.
 
    If the chunk's text changes (e.g. you edit that section), the id also
    changes — which correctly creates a NEW point, leaving the stale old
    one behind under its old id. See note below on cleaning those up.
    """
    key = f"{chunk['source']}::{chunk['text']}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))


class QdrantStore:
    def __init__(self, collection_name: str = settings.FARMING_KNOWLEDGE_BASE_COLLECTION_NAME):
        self.collection_name = collection_name
        self.client = QdrantClient(url=settings.QDRANT_URL)


    def ensure_collection(self, vector_size):
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config= qmodels.VectorParams(
                    size=vector_size,
                    distance=qmodels.Distance.COSINE
                )
            )
            print(f"Collection '{self.collection_name}' created with vector size {vector_size}.")
        else:
            print(f"Collection '{self.collection_name}' already exists.")


    def upsert_chunks(self, chunks: list[dict], vectors:list[list[float]]):
        self.client.upsert(
            collection_name=self.collection_name,
            points=qmodels.Batch(
                ids=[_chunk_id(chunk) for chunk in chunks],
                vectors=vectors,
                payloads=chunks
            )
        )


    def search(self, query_vector: list[float], top_k: int = 5, source_filter: str = None):
        query_filter = None
        if source_filter:
            query_filter = qmodels.Filter(
                must=[
                    qmodels.FieldCondition(
                        key="source",
                        match=qmodels.MatchValue(value=source_filter)
                    )
                ]
            )
            
        return self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
            query_filter=query_filter
        ).points
    