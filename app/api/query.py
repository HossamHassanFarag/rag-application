# هذا الملف مسؤول عن استقبال أسئلة المستخدم وتشغيل دورة الـ RAG وإرجاع الإجابة والمصادر المنظمة.

from fastapi import APIRouter, HTTPException

from app.rag.service import RAGService
from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter(
    prefix="/query",
    tags=["query"],
)


@router.post(
    "",
    response_model=QueryResponse,
)
def query_documents(
    request: QueryRequest,
):
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    if request.limit < 1 or request.limit > 20:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 20.",
        )

    rag_service = RAGService()

    result = rag_service.answer(
        question=request.question,
        limit=request.limit,
    )

    formatted_results = [
        {
            "text": item.payload.get(
                "text",
                "",
            ),
            "source": item.payload.get(
                "source",
                "",
            ),
            "page": item.payload.get(
                "page"
            ),
            "chunk_index": item.payload.get(
                "chunk_index",
                0,
            ),
            "score": item.score,
        }
        for item in result["results"]
    ]

    return QueryResponse(
        question=request.question,
        answer=result["answer"],
        results=formatted_results,
        citations=result["citations"],
    )