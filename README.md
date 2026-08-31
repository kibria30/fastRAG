# fastRAG

 A minimal Retrieval-Augmented Generation (RAG) demo that indexes local Markdown knowledge files and exposes simple ingestion and LLM/embedding service hooks. It ships with two selectable knowledge domains — Bangladesh law/constitution and public health/medicine — each backed by its own Qdrant collection and system prompt (see `app/domains.py`).

## Integrations & Features

- **Agent behavior with tool calling:** supports agent-style workflows where an orchestration layer can invoke local tool services (for example, `app/services/tool_services/weather_tools.py`) in a safe, auditable way.
- **FastEmbed (embedding service):** plug-in friendly, high-performance embedding adapter for low-latency local embeddings under `app/services/embedding_services/`.
- **Groq (LLM API):** support for Groq LLM endpoints via `app/services/llm_services/groqLLMService.py` for ultra-low-latency model queries.
- **Qdrant (vector DB):** recommended production-ready vector store; `app/services/vector_store_service.py` can be configured to use Qdrant for persistent, fast nearest-neighbor search.
- **LangChain (wrapper):** optional LangChain adapters let you use chains, agents, and higher-level orchestration while preserving the repo's provider-agnostic service abstractions.


## What this repo contains

- `app/` - application code (ingest, services, and main entry)
- `app/domains.py` - registry of knowledge domains (folder path, Qdrant collection, system prompt) selectable at query time
- `knowledge_base/law/` - Bangladesh law & constitution articles (sourced from Wikipedia)
- `knowledge_base/health/` - public health & medicine articles (sourced from Wikipedia)

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

4. Ingest documents into the vector store (indexes every domain in `app/domains.py` into its own Qdrant collection):

```bash
python -m app.ingest
```

5. Run the app (example):

```bash
uvicorn app.main:app --reload
```

6. Query a specific domain:

```bash
curl "http://localhost:8000/query?query=How+many+amendments+has+the+Constitution+of+Bangladesh+had?&domain=law"
curl "http://localhost:8000/query?query=What+is+stage+2+hypertension?&domain=health"
```

`domain` defaults to `law` if omitted. In Telegram, users pick a domain first by sending `/law` or `/health` (or `/start` to see the menu); the bot remembers the choice per chat for the rest of the session (in-memory, resets on restart).

## Project structure

Key modules:

- `app/ingest.py` — document ingestion pipeline
- `app/services/chunking_services/` — pluggable, file-type-aware chunking, structured like `embedding_services/`/`llm_services/`/`messaging_services/`: `baseChunkerService.py` defines the `BaseChunkerService` interface (`extensions`, `chunk(path)`), one file per concrete chunker (currently `markdownChunkerService.py`), and `__init__.py` aggregates them into `CHUNKER_SERVICES` and dispatches by extension (`chunk_file`, `chunk_folder`). To support a new file type, add a `<type>ChunkerService.py` implementing `BaseChunkerService` and list it in `CHUNKER_SERVICES`.
- `app/services/vector_store_service.py` — vector store wrapper
- `app/services/embedding_services/` — embedding providers
- `app/services/llm_services/` — LLM provider wrappers

## Adding content

Add Markdown files to `knowledge_base/law/` or `knowledge_base/health/` and re-run `python -m app.ingest`, or register a new domain (folder, collection name, system prompt) in `app/domains.py` and add its files under `knowledge_base/<key>/`.

## Contributing

Feel free to open issues or PRs. Keep changes focused and include tests where appropriate.

## License

MIT — see LICENSE (add one if needed).