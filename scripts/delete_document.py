# هذا الملف مسؤول عن حذف جميع الـ Chunks الخاصة بمستند محدد من Qdrant.

import sys

from app.vector_store.qdrant import QdrantVectorStore


def main():

    if len(sys.argv) != 2:
        print(
            "Usage: python -m scripts.delete_document <source>"
        )
        raise SystemExit(1)

    source = sys.argv[1]

    vector_store = QdrantVectorStore()

    vector_store.delete_by_source(
        source
    )

    print(
        f"Deleted document: {source}"
    )


if __name__ == "__main__":
    main()