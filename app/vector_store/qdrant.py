# هذا الملف مسؤول عن الاتصال بـ Qdrant وإدارة تخزين وحذف والبحث عن الـ Embeddings مع إعادة استخدام الاتصال.

from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
)

from app.core.config import settings
from app.vector_store.collections import create_collection


class QdrantVectorStore:

    _client = None

    def __init__(self):

        if self.__class__._client is None:
            self.__class__._client = QdrantClient(
                url=settings.qdrant_url
            )

        self.client = self.__class__._client
        self.collection_name = settings.qdrant_collection

    def ensure_collection(
        self,
        vector_size: int,
    ):
        create_collection(
            self.client,
            self.collection_name,
            vector_size,
        )

    def add_documents(
        self,
        embeddings: list[list[float]],
        payloads: list[dict],
    ):
        points = []

        for embedding, payload in zip(
            embeddings,
            payloads,
        ):
            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=embedding,
                    payload=payload,
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def delete_by_source(
        self,
        source: str,
    ):
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="source",
                        match=MatchValue(
                            value=source
                        ),
                    )
                ]
            ),
        )

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ):
        return self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
        ).points