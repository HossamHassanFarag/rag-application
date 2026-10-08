# هذا الملف مسؤول عن تنظيف النصوص المستخرجة من المستندات قبل تقسيمها إلى Chunks.

import re


def clean_text(text: str) -> str:

    text = text.replace(
        "\x00",
        " ",
    )

    text = re.sub(
        r"[ \t]*\n[ \t]*",
        "\n",
        text,
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    return text.strip()