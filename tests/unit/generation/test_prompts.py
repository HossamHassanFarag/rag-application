# هذا الملف مسؤول عن اختبار بناء الرسائل التي سيتم إرسالها إلى نموذج اللغة.

from app.generation.prompts import build_messages


def test_build_messages():

    context = (
        "[Source 1]\n"
        "Source: python.txt\n\n"
        "Python is a high-level programming language."
    )

    messages = build_messages(
        question="What is Python?",
        context=context,
    )

    assert len(messages) == 2

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"

    assert "Python is a high-level programming language." in (
        messages[1]["content"]
    )

    assert "What is Python?" in messages[1]["content"]