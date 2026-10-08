# هذا الملف مسؤول عن تجميع إعدادات المشروع وقراءتها من ملف البيئة .env.

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "rag_documents"

    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    hf_token: str
    hf_model: str = "openai/gpt-oss-120b:fastest"
    hf_base_url: str = "https://router.huggingface.co/v1"

    chunk_size: int = 500
    chunk_overlap: int = 50

    retrieval_score_threshold: float = 0.50

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()