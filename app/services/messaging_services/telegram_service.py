import httpx

from app.config import settings
from app.services.messaging_services.base_messaging_service import BaseMessagingService
from app.services.telegram_formatting import format_for_telegram


TELEGRAM_API = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"


class TelegramService(BaseMessagingService):
    def parse_incoming(self, payload: dict) -> tuple[str, str] | None:
        message = payload.get("message")
        if not message or "text" not in message:
            return None

        chat_id = str(message["chat"]["id"])
        text = message["text"]
        return chat_id, text


    async def send_message(self, chat_id: str, text: str) -> None:
        safe_text = format_for_telegram(text)
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{TELEGRAM_API}/sendMessage",
                json={"chat_id": chat_id, "text": safe_text, "parse_mode": "Markdown"},
            )
            if response.status_code != 200:
                response = await client.post(
                    f"{TELEGRAM_API}/sendMessage",
                    json={"chat_id": chat_id, "text": safe_text},
                )
            response.raise_for_status()
