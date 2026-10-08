# هذا الملف مسؤول عن اختيار أداة القراءة المناسبة حسب امتداد الملف.

from pathlib import Path

from app.ingestion.loaders.docx import load_docx
from app.ingestion.loaders.pdf import load_pdf
from app.ingestion.loaders.text import load_text


def get_loader(file_path: str):
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return load_pdf

    if extension == ".docx":
        return load_docx

    if extension in {".txt", ".md"}:
        return load_text

    raise ValueError(
        f"Unsupported file type: {extension}"
    )