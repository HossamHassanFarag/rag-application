# هذا الملف مسؤول عن تشغيل عملية إدخال مستند محدد إلى نظام الـ RAG.

import sys
from pathlib import Path

from app.documents.service import DocumentService


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.ingest <file_path>")
        raise SystemExit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"File not found: {path}")
        raise SystemExit(1)

    count = DocumentService().ingest(
        str(path)
    )

    print(f"Inserted chunks: {count}")


if __name__ == "__main__":
    main()