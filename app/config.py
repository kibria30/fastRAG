from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(default="your_api_key", env="OPENAI_API_KEY")
    OPENAI_MODEL: str = Field(default="gpt-4o-mini", env="OPENAI_MODEL")
    OPENAI_EMBEDDING_MODEL: str = Field(default="text-embedding-3-small", env="OPENAI_EMBEDDING_MODEL")
    OPENROUTER_API_KEY: str = Field(default="your_openrouter_api_key", env="OPENROUTER_API_KEY")
    OPENROUTER_PRIMARY_MODEL: str = Field(default="openai/gpt-oss-20b", env="OPENROUTER_PRIMARY_MODEL")
    OPENROUTER_FALLBACK_MODEL: str = Field(default="openrouter/free", env="OPENROUTER_FALLBACK_MODEL")
    QDRANT_URL:str = Field(default="http://localhost:6333", env="QDRANT_URL")
    CHUNK_SIZE: int = Field(default=500, env="CHUNK_SIZE")
    CHUNK_OVERLAP: int = Field(default=50, env="CHUNK_OVERLAP")
    GROQ_MODEL: str = Field(default="llama-3.1-8b-instant", env="GROQ_MODEL")
    GROQ_API_KEY: str = Field(default="your_groq_api_key", env="GROQ_API_KEY")
    TELEGRAM_BOT_TOKEN: str = Field(default="your_telegram_bot_token", env="TELEGRAM_BOT_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()