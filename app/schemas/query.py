# هذا الملف مسؤول عن تعريف شكل البيانات التي يستقبلها ويرجعها Query API.

from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
    limit: int = 5


class SourceResponse(BaseModel):
    text: str
    source: str
    page: int | None
    chunk_index: int
    score: float


class CitationResponse(BaseModel):
    id: int
    source: str
    page: int | None
    chunk_index: int
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    results: list[SourceResponse]
    citations: list[CitationResponse]