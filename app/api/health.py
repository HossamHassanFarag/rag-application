# هذا الملف مسؤول عن توفير endpoint للتأكد من أن الـ FastAPI Backend يعمل بشكل صحيح.

from fastapi import APIRouter


router = APIRouter(
    prefix="/api",
)


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "rag-application",
    }