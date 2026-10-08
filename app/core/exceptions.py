# هذا الملف يعرّف أخطاء مخصصة يمكن استخدامها لتوضيح مشاكل الـ RAG بدلاً من أخطاء عامة.
class RAGError(Exception):
    pass

class DocumentProcessingError(RAGError):
    pass

class VectorStoreError(RAGError):
    pass
