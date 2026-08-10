# fastRAG

 A minimal Retrieval-Augmented Generation (RAG) demo that indexes local Markdown knowledge files and exposes simple ingestion and LLM/embedding service hooks.

## Integrations & Features

- **Agent behavior with tool calling:** supports agent-style workflows where an orchestration layer can invoke local tool services (for example, `app/services/tool_services/weather_tools.py`) in a safe, auditable way.
- **FastEmbed (embedding service):** plug-in friendly, high-performance embedding adapter for low-latency local embeddings under `app/services/embedding_services/`.
- **Groq (LLM API):** support for Groq LLM endpoints via `app/services/llm_services/groqLLMService.py` for ultra-low-latency model queries.
- **Qdrant (vector DB):** recommended production-ready vector store; `app/services/vector_store_service.py` can be configured to use Qdrant for persistent, fast nearest-neighbor search.
- **LangChain (wrapper):** optional LangChain adapters let you use chains, agents, and higher-level orchestration while preserving the repo's provider-agnostic service abstractions.


## What this repo contains

- `app/` - application code (ingest, services, and main entry)
- `knowledge_base/` - sample Markdown documents used as the knowledge store

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (if a `requirements.txt` exists):

```bash
pip install -r requirements.txt
```

3. Configure credentials/settings in `app/config.py` as needed (API keys, endpoints).

4. Ingest documents into the vector store:

```bash
python -m app.ingest
```

5. Run the app (example):

```bash
uvicorn app.main:app --reload
```

## Project structure

Key modules:

- `app/ingest.py` — document ingestion and chunking pipeline
- `app/services/chunking.py` — text chunking utilities
- `app/services/vector_store_service.py` — vector store wrapper
- `app/services/embedding_services/` — embedding providers
- `app/services/llm_services/` — LLM provider wrappers

## Adding content

Add Markdown files to the `knowledge_base/` folder and run the ingestion step to index them.

## Integrations & Features

- **Agent behavior with tool calling:** supports agent-style workflows where an orchestration layer can invoke local tool services (for example, `app/services/tool_services/weather_tools.py`) in a safe, auditable way.
- **FastEmbed (embedding service):** plug-in friendly, high-performance embedding adapter for low-latency local embeddings under `app/services/embedding_services/`.
- **Groq (LLM API):** support for Groq LLM endpoints via `app/services/llm_services/groqLLMService.py` for ultra-low-latency model queries.
- **Qdrant (vector DB):** recommended production-ready vector store; `app/services/vector_store_service.py` can be configured to use Qdrant for persistent, fast nearest-neighbor search.
- **LangChain (wrapper):** optional LangChain adapters let you use chains, agents, and higher-level orchestration while preserving the repo's provider-agnostic service abstractions.

## Contributing

Feel free to open issues or PRs. Keep changes focused and include tests where appropriate.

## License

MIT — see LICENSE (add one if needed).