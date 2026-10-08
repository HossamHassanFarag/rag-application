# هذا الملف مسؤول عن إرسال الـ Prompts إلى نموذج اللغة من خلال Hugging Face Inference Providers والتحقق من نتيجة النموذج.

from openai import OpenAI

from app.core.config import settings
from app.generation.base import BaseGenerator


class HuggingFaceGenerator(BaseGenerator):

    def __init__(self):
        self.client = OpenAI(
            base_url=settings.hf_base_url,
            api_key=settings.hf_token,
        )

    def generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:

        response = self.client.chat.completions.create(
            model=settings.hf_model,
            messages=messages,
            max_tokens=500,
            temperature=0.2,
        )

        if not response.choices:
            raise RuntimeError(
                "The language model returned no choices."
            )

        content = response.choices[0].message.content

        if not content or not content.strip():
            raise RuntimeError(
                "The language model returned an empty response."
            )

        return content.strip()