# هذا الملف مسؤول عن واجهة المحادثة وعرض إجابة الـ RAG والمصادر الرسمية المرتبطة بها.

import streamlit as st


def render_chat(api_client):

    st.subheader("Ask a Question")

    question = st.text_input(
        "Enter your question",
        placeholder="Ask something about your documents...",
    )

    limit = st.slider(
        "Number of sources",
        min_value=1,
        max_value=10,
        value=3,
    )

    if st.button("Ask"):

        if not question.strip():
            st.warning(
                "Please enter a question."
            )
            return

        try:
            with st.spinner(
                "Searching and generating answer..."
            ):
                result = api_client.query(
                    question,
                    limit,
                )

            st.markdown("### Answer")

            st.write(
                result["answer"]
            )

            st.divider()

            st.markdown("### Sources")

            citations = result.get(
                "citations",
                [],
            )

            if not citations:
                st.info(
                    "No relevant sources were found."
                )
                return

            for citation in citations:

                source = citation.get(
                    "source",
                    "Unknown",
                )

                page = citation.get(
                    "page"
                )

                score = citation.get(
                    "score",
                    0,
                )

                title = (
                    f"Source {citation['id']}: "
                    f"{source}"
                )

                if page is not None:
                    title += (
                        f" — Page {page}"
                    )

                with st.expander(title):

                    st.caption(
                        f"Relevance Score: {score:.4f}"
                    )

                    st.write(
                        f"Chunk: "
                        f"{citation['chunk_index']}"
                    )

                    matching_result = next(
                        (
                            item
                            for item in result["results"]
                            if item["source"] == source
                            and item["page"] == page
                            and item["chunk_index"]
                            == citation["chunk_index"]
                        ),
                        None,
                    )

                    if matching_result:
                        st.write(
                            matching_result["text"]
                        )

        except Exception as exc:
            st.error(
                f"Query failed: {exc}"
            )