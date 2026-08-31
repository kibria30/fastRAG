from abc import ABC, abstractmethod


class BaseChunkerService(ABC):
    extensions: tuple[str, ...] = ()

    @abstractmethod
    def chunk(self, path: str) -> list[dict]:
        raise NotImplementedError("Subclasses should implement this method.")
