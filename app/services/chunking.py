import os
from app.config import settings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


def chunk_markdown_file(path:str) -> list[dict]:
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


def chunk_folder(docs_folder:str) -> list[dict]:
    import glob

    md_files = sorted(glob.glob(os.path.join(docs_folder, '**/*.md'), recursive=True))

    if not md_files:
        raise FileNotFoundError(f"No markdown files found in folder: {docs_folder}")

    all_chunks = []
    for path in md_files:
        chunks = chunk_markdown_file(path)
        all_chunks.extend(chunks)
    return all_chunks
