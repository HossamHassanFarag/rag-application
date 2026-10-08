# هذا الملف مسؤول عن إنشاء والتحقق من وجود Collections داخل Qdrant.

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


def create_collection(
    client: QdrantClient,
    collection_name: str,
    vector_size: int,
) -> None:
    collections = client.get_collections().collections

    if any(
        collection.name == collection_name
        for collection in collections
    ):
        return

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE,
        ),
    )