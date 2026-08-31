from fastapi import FastAPI, Request, HTTPException
from app.services.embedding_services.localEmbeddingsService import LocalEmbeddingsService
import time
from app.domains import DOMAINS, DEFAULT_DOMAIN
from app.services.vector_store_service import QdrantStore
from app.services.llm_services.openRouterLLMService import OpenRouterLLMService
from app.services.llm_services.groqLLMService import GroqLLMService
from app.services.llm_services.gptLLMService import GPTLLMService
from app.services.messaging_services.telegram_service import TelegramService


app = FastAPI()


embedder = LocalEmbeddingsService()
stores = {key: QdrantStore(collection_name=domain["collection"]) for key, domain in DOMAINS.items()}
# llm = OpenRouterLLMService()
llm = GroqLLMService()
# llm = GPTLLMService()
telegram = TelegramService()

# In-memory per-chat domain selection for the Telegram bot. Resets on restart.
chat_domains: dict[str, str] = {}


async def answer_query(query: str, domain: str = DEFAULT_DOMAIN, top_k: int = 5, source: str = None):
    if domain not in DOMAINS:
        raise HTTPException(status_code=400, detail=f"Unknown domain '{domain}'. Valid domains: {', '.join(DOMAINS)}")

    start_time = time.time()
    query_vector = embedder.embed(query)[0]
    results = stores[domain].search(query_vector, top_k=top_k, source_filter=source)
    chunks = [r.payload for r in results]

    after_retrieval = time.time()
    retrieval_time = after_retrieval - start_time

    result = await llm.generate_answer(query, chunks, domain=domain)
    llm_generation_time = time.time() - after_retrieval

    return {
        "query": query,
        "domain": domain,
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
async def query(query: str, domain: str = DEFAULT_DOMAIN, top_k: int = 5, source: str = None):
    return await answer_query(query, domain, top_k, source)


def _domain_menu_text() -> str:
    lines = ["Please choose a knowledge base by sending its command:"]
    for key, domain in DOMAINS.items():
        lines.append(f"/{key} — {domain['label']}")
    return "\n".join(lines)


@app.post("/webhook/telegram")
async def telegram_webhook(request: Request):
    payload = await request.json()
    parsed = telegram.parse_incoming(payload)

    if parsed is None:
        return {"ok": True}

    chat_id, text = parsed
    stripped = text.strip().lstrip("/").lower()

    if stripped in ("start", "domain", "domains", "menu"):
        await telegram.send_message(chat_id, _domain_menu_text())
        return {"ok": True}

    if stripped in DOMAINS:
        chat_domains[chat_id] = stripped
        await telegram.send_message(chat_id, f"Knowledge base set to: {DOMAINS[stripped]['label']}. Ask away.")
        return {"ok": True}

    domain = chat_domains.get(chat_id)
    if domain is None:
        await telegram.send_message(chat_id, _domain_menu_text())
        return {"ok": True}

    result = await answer_query(text, domain)
    await telegram.send_message(chat_id, result["answers"])

    return {"ok": True}
