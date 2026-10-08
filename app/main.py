# هذا الملف هو نقطة تشغيل الـ FastAPI Backend وتجميع جميع API Routers الخاصة بالمشروع.

from fastapi import FastAPI

from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.api.query import router as query_router


app = FastAPI(
    title="AI Knowledge Assistant",
    description="Retrieval-Augmented Generation API",
    version="1.0.0",
)


app.include_router(health_router)
app.include_router(documents_router)
app.include_router(query_router)