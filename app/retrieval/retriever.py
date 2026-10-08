# هذا الملف مسؤول عن تحويل سؤال المستخدم إلى Embedding والبحث عن النتائج ذات الصلة داخل Qdrant.

from app.core.config import settings
from app.embeddings.sentence_transformer import SentenceTransformerEmbeddingService
from app.vector_store.qdrant import QdrantVectorStore


class Retriever:

    def __init__(self):
        self.embedding_service = SentenceTransformerEmbeddingService()
        self.vector_store = QdrantVectorStore()

    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ):
        query_vector = self.embedding_service.embed_text(
            query
        )

        results = self.vector_store.search(
            query_vector,
            limit,
        )

        filtered_results = [
            result
            for result in results
            if result.score >= settings.retrieval_score_threshold
        ]

        return filtered_results