# هذا الملف مسؤول عن تحويل نتائج الـ Retrieval إلى بيانات مصادر منظمة يمكن عرضها للمستخدم.

def build_citations(results) -> list[dict]:

    citations = []

    for index, result in enumerate(
        results,
        start=1,
    ):
        payload = result.payload or {}

        citations.append(
            {
                "id": index,
                "source": payload.get(
                    "source",
                    "Unknown",
                ),
                "page": payload.get(
                    "page"
                ),
                "chunk_index": payload.get(
                    "chunk_index",
                    0,
                ),
                "score": round(
                    result.score,
                    4,
                ),
            }
        )

    return citations