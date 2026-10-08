# هذا الملف يحتوي على نماذج الطلبات والاستجابات المتعلقة بالمستندات.
from pydantic import BaseModel

class DocumentResponse(BaseModel):
    filename: str
    chunks: int
    status: str
