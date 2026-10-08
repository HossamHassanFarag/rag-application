# هذا الملف مسؤول عن توفير خدمة RAG جاهزة للاستخدام من طبقة الـ API.

from app.rag.pipeline import RAGPipeline


class RAGService:

    def __init__(self):
        self.pipeline = RAGPipeline()

    def answer(
        self,
        question: str,
        limit: int = 5,
    ) -> dict:

        return self.pipeline.run(
            question=question,
            limit=limit,
        )