# هذا الملف مسؤول عن تحويل نتائج الـ Retrieval إلى Context منظم يمكن إرساله إلى نموذج اللغة.

def build_context(results) -> str:
    if not results:
        return "No relevant documents were found."

    context_parts = []

    for index, result in enumerate(results, start=1):
        payload = result.payload

        source = payload.get("source", "Unknown")
        page = payload.get("page")
        score = result.score
        text = payload.get("text", "").strip()

        source_info = f"Source: {source}"

        if page is not None:
            source_info += f", Page: {page}"

        context_parts.append(
            f"[Source {index}]\n"
            f"{source_info}\n"
            f"Relevance Score: {score:.4f}\n\n"
            f"{text}"
        )

    return "\n\n---\n\n".join(context_parts)