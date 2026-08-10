from abc import ABC, abstractmethod


class BaseMessagingService(ABC):
    @abstractmethod
    def parse_incoming(self, payload: dict) -> tuple[str, str] | None:
        raise NotImplementedError("Subclasses should implement this method.")


    @abstractmethod
    async def send_message(self, chat_id: str, text: str) -> None:
        raise NotImplementedError("Subclasses should implement this method.")