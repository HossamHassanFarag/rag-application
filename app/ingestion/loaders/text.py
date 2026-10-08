# هذا الملف مسؤول عن قراءة الملفات النصية مثل TXT و Markdown.

from pathlib import Path


def load_text(file_path: str) -> list[dict]:
    path = Path(file_path)

    text = path.read_text(
        encoding="utf-8",
        errors="ignore",
    )

    if not text.strip():
        return []

    return [
        {
            "text": text,
            "page": None,
            "source": path.name,
        }
    ]