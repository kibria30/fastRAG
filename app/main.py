from fastapi import FastAPI, Request
from app.services.embedding_services.localEmbeddingsService import LocalEmbeddingsService
import time
from app.config import settings
from app.services.vector_store_service import QdrantStore
from app.services.llm_services.openRouterLLMService import OpenRouterLLMService
from app.services.llm_services.groqLLMService import GroqLLMService
from app.services.llm_services.gptLLMService import GPTLLMService
from app.services.messaging_services.telegram_service import TelegramService


app = FastAPI()


embedder = LocalEmbeddingsService()
store = QdrantStore(collection_name=settings.FARMING_KNOWLEDGE_BASE_COLLECTION_NAME)
# llm = OpenRouterLLMService()
llm = GroqLLMService()
# llm = GPTLLMService()
telegram = TelegramService()


async def answer_query(query: str, top_k: int = 5, source: str = None):
    start_time = time.time()
    query_vector = embedder.embed(query)[0]
    results = store.search(query_vector, top_k=top_k, source_filter=source)
    chunks = [r.payload for r in results]

    after_retrieval = time.time()
    retrieval_time = after_retrieval - start_time

    result = await llm.generate_answer(query, chunks)
    llm_generation_time = time.time() - after_retrieval

    return {
        "query": query,
        "answers": result["content"],
        "tools_used": result["tools_used"],
        "sources": [
            {
                "source": c.get("source"),
                "text": c.get("text"),
            }
            for c in chunks
        ],
        "time_taken": time.time() - start_time,
        "retrieval_time": retrieval_time,
        "llm_generation_time": llm_generation_time
    }


@app.get("/query")
async def query(query: str, top_k: int = 5, source: str = None):
    return await answer_query(query, top_k, source)


@app.post("/webhook/telegram")
async def telegram_webhook(request: Request):
    payload = await request.json()
    parsed = telegram.parse_incoming(payload)

    if parsed is None:
        return {"ok": True}   

    chat_id, text = parsed
    result = await answer_query(text)
    
    await telegram.send_message(chat_id, result["answers"])

    return {"ok": True}