# هذا الملف مسؤول عن اختبار HuggingFaceGenerator بدون إرسال طلب حقيقي إلى Hugging Face.

from unittest.mock import MagicMock, patch

from app.generation.huggingface import HuggingFaceGenerator


def test_generate():

    messages = [
        {
            "role": "user",
            "content": "What is Python?",
        }
    ]

    mock_response = MagicMock()

    mock_response.choices[0].message.content = (
        "Python is a programming language."
    )

    with patch(
        "app.generation.huggingface.OpenAI"
    ) as mock_openai:

        mock_openai.return_value.chat.completions.create.return_value = (
            mock_response
        )

        generator = HuggingFaceGenerator()

        answer = generator.generate(messages)

        assert answer == (
            "Python is a programming language."
        )