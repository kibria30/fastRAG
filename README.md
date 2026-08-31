# fastRAG

Retrieval-Augmented Generation API with a Telegram bot front-end — indexes Markdown knowledge bases into Qdrant and answers questions across multiple selectable domains with tool-calling LLM agents.

Built provider-agnostic from the ground up: every LLM, embedding model, and chunker sits behind its own interface, so the stack swaps or scales to new domains and providers without touching core logic.

## Features

- 🧠 Swappable LLM backends — Groq, OpenAI, and OpenRouter behind one interface, picked at runtime
- 🔎 Swappable embedding models — local FastEmbed or OpenAI embeddings behind one interface
- 🛠️ Agentic tool calling — LLM invokes local tools only when context can't answer
- 📄 Pluggable ingestion pipeline — file-type-aware chunking, extensible to new formats
- 🤖 Telegram bot — webhook-driven chat interface with per-user domain selection
- 🐳 Containerized — one-command deploy with Docker Compose
- 🔀 Multi-domain RAG — pluggable knowledge domains (law, health), each with its own vector collection and system prompt

## Tech Stack

**API & Runtime:** Python · FastAPI · Uvicorn · Pydantic

**AI / RAG:** Qdrant (vector DB) · FastEmbed · LangChain · Groq · OpenAI · OpenRouter

**Messaging:** Telegram Bot API

**Infra:** Docker · Docker Compose
