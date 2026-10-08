# هذا الملف مسؤول عن تنفيذ دورة الـ RAG الكاملة من السؤال حتى توليد الإجابة وتجهيز المصادر.

from app.generation.generator import get_generator
from app.generation.prompts import build_messages
from app.rag.citations import build_citations
from app.rag.context_builder import build_context
from app.retrieval.retriever import Retriever


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.generator = get_generator()

    def run(
        self,
        question: str,
        limit: int = 5,
    ) -> dict:

        results = self.retriever.retrieve(
            question,
            limit=limit,
        )

        context = build_context(results)

        messages = build_messages(
            question=question,
            context=context,
        )

        answer = self.generator.generate(
            messages
        )

        citations = build_citations(
            results
        )

        return {
            "answer": answer,
            "results": results,
            "citations": citations,
        }