# هذا الملف يختبر تقسيم النص إلى chunks مع overlap.
from app.ingestion.chunker import chunk_text
def test_chunker(): assert len(chunk_text("a"*100, 30, 5)) > 1
