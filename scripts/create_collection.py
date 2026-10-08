# هذا الملف مسؤول عن إنشاء Collection في Qdrant بالحجم الصحيح للـ Embeddings المستخدمة في المشروع.

from app.embeddings.sentence_transformer import SentenceTransformerEmbeddingService
from app.vector_store.qdrant import QdrantVectorStore


def main():
    embedding_service = SentenceTransformerEmbeddingService()
    vector_store = QdrantVectorStore()

    dimension = embedding_service.dimension()

    vector_store.ensure_collection(dimension)

    print("Collection created successfully.")
    print(f"Vector dimension: {dimension}")


if __name__ == "__main__":
    main()