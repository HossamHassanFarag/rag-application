# هذا الملف مسؤول عن تنسيق عملية إدخال وتحديث المستندات من مرحلة الـ Ingestion حتى تخزين الـ Embeddings في Qdrant.

from uuid import uuid4

from app.embeddings.sentence_transformer import SentenceTransformerEmbeddingService
from app.ingestion.pipeline import process_document
from app.vector_store.qdrant import QdrantVectorStore


class DocumentService:

    def __init__(self):
        self.embedding_service = SentenceTransformerEmbeddingService()
        self.vector_store = QdrantVectorStore()

        self.vector_store.ensure_collection(
            self.embedding_service.dimension()
        )

    def ingest(
        self,
        file_path: str,
        source_name: str | None = None,
    ) -> int:

        chunks = process_document(file_path)

        if not chunks:
            return 0

        source = source_name or chunks[0]["source"]

        self.vector_store.delete_by_source(
            source
        )

        document_id = str(uuid4())

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.embedding_service.embed_texts(
            texts
        )

        payloads = [
            {
                "document_id": document_id,
                "text": chunk["text"],
                "source": source,
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"],
            }
            for chunk in chunks
        ]

        self.vector_store.add_documents(
            embeddings,
            payloads,
        )

        return len(chunks)