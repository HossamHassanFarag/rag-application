# هذا الملف مسؤول عن تنفيذ عملية تجهيز المستند من القراءة والتنظيف والتقسيم حتى إنتاج البيانات الجاهزة للـ Embeddings.

from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text
from app.ingestion.loaders.factory import get_loader


def process_document(file_path: str) -> list[dict]:
    loader = get_loader(file_path)
    loaded_documents = loader(file_path)

    chunks = []

    for document in loaded_documents:
        cleaned = clean_text(document["text"])

        if not cleaned:
            continue

        document_chunks = chunk_text(cleaned)

        for index, chunk in enumerate(document_chunks):
            chunks.append(
                {
                    "text": chunk,
                    "source": document["source"],
                    "page": document["page"],
                    "chunk_index": index,
                }
            )

    return chunks