# هذا الملف مسؤول عن تحميل نموذج الـ Embeddings مرة واحدة وإعادة استخدامه في جميع عمليات المشروع.

from sentence_transformers import SentenceTransformer

from app.core.config import settings


class SentenceTransformerEmbeddingService:

    _model = None

    def __init__(self):
        if self.__class__._model is None:
            self.__class__._model = SentenceTransformer(
                settings.embedding_model
            )

        self.model = self.__class__._model

    def embed_text(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()

    def dimension(self) -> int:
        return self.model.get_embedding_dimension()
