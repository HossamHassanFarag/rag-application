# هذا الملف مسؤول عن قراءة ملفات Word واستخراج النص من الفقرات.

from pathlib import Path

from docx import Document


def load_docx(file_path: str) -> list[dict]:
    document = Document(file_path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )

    if not text.strip():
        return []

    return [
        {
            "text": text,
            "page": None,
            "source": Path(file_path).name,
        }
    ]