# هذا الملف مسؤول عن واجهة رفع المستندات وإظهار نتيجة عملية الإدخال للمستخدم.

import streamlit as st


def render_upload(api_client):

    st.subheader("Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=[
            "pdf",
            "docx",
            "txt",
            "md",
        ],
    )

    if uploaded_file is None:
        return

    st.caption(
        f"Selected file: {uploaded_file.name}"
    )

    if st.button("Upload Document"):

        try:
            with st.spinner(
                "Processing document..."
            ):

                result = api_client.upload_document(
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                )

            st.success(
                f"Document processed successfully. "
                f"{result['chunks_inserted']} chunks inserted."
            )

        except Exception as exc:
            st.error(
                f"Upload failed: {exc}"
            )