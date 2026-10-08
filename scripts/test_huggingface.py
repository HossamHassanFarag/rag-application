# هذا الملف مسؤول عن اختبار الاتصال بـ Hugging Face API والتأكد من أن الـ Token والموديل يعملان بشكل صحيح.

from openai import OpenAI

from app.core.config import settings


def main():
    client = OpenAI(
        base_url=settings.hf_base_url,
        api_key=settings.hf_token,
    )

    response = client.chat.completions.create(
        model=settings.hf_model,
        messages=[
            {
                "role": "user",
                "content": "Explain what Python is in one sentence.",
            }
        ],
        max_tokens=100,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
