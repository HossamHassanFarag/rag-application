# هذا الملف مخصص لعناصر الـ Sidebar مثل الإعدادات ورفع الملفات.
# هذا الملف مسؤول عن عرض معلومات وإعدادات المشروع في الشريط الجانبي.

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("AI Knowledge Assistant")

        st.markdown(
            """
            Retrieval-Augmented Generation
            """
        )

        st.divider()

        st.caption(
            "Backend: FastAPI"
        )

        st.caption(
            "Vector Database: Qdrant"
        )

        st.caption(
            "Embeddings: Sentence Transformers"
        )

        st.caption(
            "LLM: Ollama"
        )