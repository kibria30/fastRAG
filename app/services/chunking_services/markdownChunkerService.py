import os

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

from app.config import settings
from app.services.chunking_services.baseChunkerService import BaseChunkerService


class MarkdownChunkerService(BaseChunkerService):
    extensions = (".md", ".markdown")

    def chunk(self, path: str) -> list[dict]:
        with open(path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")])
        header_chunks = header_splitter.split_text(raw_text)
        size_splitter = RecursiveCharacterTextSplitter(chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP)
        final_chunks = []
        for doc in header_chunks:
            header_path = " > ".join(v for k, v in doc.metadata.items() if k in ("h1", "h2", "h3"))
            for sub_text in size_splitter.split_text(doc.page_content):
                text_with_context = f"{header_path}\n{sub_text}" if header_path else sub_text
                final_chunks.append({
                    "text": text_with_context,
                    "source": os.path.basename(path),
                    **doc.metadata,
                })
        return final_chunks
