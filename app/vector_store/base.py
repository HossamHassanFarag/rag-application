# هذا الملف يعرّف الواجهة العامة لقاعدة المتجهات المستخدمة في التطبيق.
from abc import ABC, abstractmethod

class VectorStore(ABC):
    @abstractmethod
    def upsert(self, vectors, payloads): ...
    @abstractmethod
    def search(self, vector, top_k=5): ...
