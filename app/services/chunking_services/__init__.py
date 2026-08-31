import glob
import os

from app.services.chunking_services.markdownChunkerService import MarkdownChunkerService

CHUNKER_SERVICES = [
    MarkdownChunkerService(),
]

_EXTENSION_MAP = {
    ext: chunker
    for chunker in CHUNKER_SERVICES
    for ext in chunker.extensions
}


def supported_extensions() -> list[str]:
    return list(_EXTENSION_MAP)


def chunk_file(path: str) -> list[dict]:
    ext = os.path.splitext(path)[1].lower()
    chunker = _EXTENSION_MAP.get(ext)
    if chunker is None:
        raise ValueError(
            f"No chunker registered for file type '{ext}' (file: {path}). "
            f"Supported: {supported_extensions()}"
        )
    return chunker.chunk(path)


def chunk_folder(docs_folder: str) -> list[dict]:
    all_files: set[str] = set()
    for ext in supported_extensions():
        all_files.update(glob.glob(os.path.join(docs_folder, f"**/*{ext}"), recursive=True))

    if not all_files:
        raise FileNotFoundError(
            f"No supported files found in folder: {docs_folder} "
            f"(supported: {supported_extensions()})"
        )

    all_chunks = []
    for path in sorted(all_files):
        all_chunks.extend(chunk_file(path))
    return all_chunks
