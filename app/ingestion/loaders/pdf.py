# هذا الملف مسؤول عن قراءة ملفات PDF واستخراج النص مع رقم الصفحة.

from pathlib import Path

from pypdf import PdfReader


def load_pdf(file_path: str) -> list[dict]:
    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            documents.append(
                {
                    "text": text,
                    "page": page_number,
                    "source": Path(file_path).name,
                }
            )

    return documents