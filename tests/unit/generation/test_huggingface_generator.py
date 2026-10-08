# هذا الملف مسؤول عن اختبار التعامل مع نتائج Hugging Face الفارغة أو غير الصالحة.

from unittest.mock import MagicMock, patch

import pytest

from app.generation.huggingface import HuggingFaceGenerator


def test_empty_llm_response():

    generator = HuggingFaceGenerator()

    mock_response = MagicMock()

    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                content=""
            )
        )
    ]

    with patch.object(
        generator.client.chat.completions,
        "create",
        return_value=mock_response,
    ):

        with pytest.raises(
            RuntimeError,
            match="empty response",
        ):

            generator.generate(
                [
                    {
                        "role": "user",
                        "content": "Hello",
                    }
                ]
            )