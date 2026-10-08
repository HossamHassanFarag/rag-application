# هذا الملف يحتوي على نماذج بيانات مشتركة مثل معلومات المصادر.
from pydantic import BaseModel

class Source(BaseModel):
    filename: str
    chunk_id: str
    score: float
    text: str
