from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from app.rag.pipeline import RAGPipeline


def test_pipeline_retrieves_builds_context_generates_answer_and_citations():
    retrieved = [
        SimpleNamespace(
            score=0.92,
            payload={
                "text": "Python is a programming language.",
                "source": "python.txt",
                "page": 2,
                "chunk_index": 3,
            },
        )
    ]

    fake_retriever = MagicMock()
    fake_retriever.retrieve.return_value = retrieved

    fake_generator = MagicMock()
    fake_generator.generate.return_value = (
        "Python is a programming language."
    )

    with (
        patch(
            "app.rag.pipeline.Retriever",
            return_value=fake_retriever,
        ),
        patch(
            "app.rag.pipeline.get_generator",
            return_value=fake_generator,
        ),
    ):
        pipeline = RAGPipeline()
        result = pipeline.run(
            question="What is Python?",
            limit=3,
        )

    fake_retriever.retrieve.assert_called_once_with(
        "What is Python?",
        limit=3,
    )

    fake_generator.generate.assert_called_once()
    messages = fake_generator.generate.call_args.args[0]

    assert messages[0]["role"] == "system"
    assert "Python is a programming language." in messages[1]["content"]
    assert "What is Python?" in messages[1]["content"]

    assert result["answer"] == "Python is a programming language."
    assert result["results"] == retrieved
    assert result["citations"] == [
        {
            "id": 1,
            "source": "python.txt",
            "page": 2,
            "chunk_index": 3,
            "score": 0.92,
        }
    ]


def test_pipeline_handles_no_retrieved_documents():
    fake_retriever = MagicMock()
    fake_retriever.retrieve.return_value = []

    fake_generator = MagicMock()
    fake_generator.generate.return_value = (
        "The information is not available in the provided documents."
    )

    with (
        patch(
            "app.rag.pipeline.Retriever",
            return_value=fake_retriever,
        ),
        patch(
            "app.rag.pipeline.get_generator",
            return_value=fake_generator,
        ),
    ):
        pipeline = RAGPipeline()
        result = pipeline.run("Unknown question")

    assert result["results"] == []
    assert result["citations"] == []
    assert result["answer"]
    fake_generator.generate.assert_called_once()
