# هذا الملف مسؤول عن اختبار تحويل نتائج الـ Retrieval إلى Context منظم.

from types import SimpleNamespace

from app.rag.context_builder import build_context


def test_build_context():

    results = [
        SimpleNamespace(
            score=0.8119,
            payload={
                "source": "python.txt",
                "page": None,
                "text": (
                    "Python is a high-level programming language. "
                    "Python is widely used for web development, "
                    "automation, data analysis, and artificial intelligence."
                ),
            },
        )
    ]

    context = build_context(results)

    assert "Source: python.txt" in context
    assert "0.8119" in context
    assert "Python is a high-level programming language." in context