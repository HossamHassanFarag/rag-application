# هذا الملف يعرّف الواجهة العامة لأي مزود Embeddings حتى يمكن تغييره بدون تعديل باقي المشروع.
from abc import ABC, abstractmethod

class EmbeddingProvider(ABC):
    @abstractmethod
    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...
    @abstractmethod
    def embed_query(self, text: str) -> list[float]: ...
