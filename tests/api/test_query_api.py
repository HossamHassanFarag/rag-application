from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_query_returns_answer_and_sources():
    mock_result = {
        "answer": "Python is a programming language.",
        "results": [
            MagicMock(
                payload={
                    "text": "Python is a high-level language.",
                    "source": "python.txt",
                    "page": 1,
                    "chunk_index": 0,
                },
                score=0.91,
            )
        ],
        "citations": [
            {
                "id": 1,
                "source": "python.txt",
                "page": 1,
                "chunk_index": 0,
                "score": 0.91,
            }
        ],
    }

    with patch("app.api.query.RAGService") as mock_service:
        mock_service.return_value.answer.return_value = mock_result

        response = client.post(
            "/query",
            json={
                "question": "What is Python?",
                "limit": 5,
            },
        )

    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What is Python?"
    assert data["answer"] == "Python is a programming language."
    assert len(data["results"]) == 1
    assert data["results"][0]["source"] == "python.txt"
    assert len(data["citations"]) == 1


def test_query_rejects_blank_question():
    with patch("app.api.query.RAGService") as mock_service:
        response = client.post(
            "/query",
            json={"question": "   ", "limit": 5},
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Question cannot be empty."
    mock_service.assert_not_called()


def test_query_rejects_limit_above_maximum():
    with patch("app.api.query.RAGService") as mock_service:
        response = client.post(
            "/query",
            json={"question": "What is Python?", "limit": 21},
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Limit must be between 1 and 20."
    mock_service.assert_not_called()


def test_query_rejects_limit_below_minimum():
    with patch("app.api.query.RAGService") as mock_service:
        response = client.post(
            "/query",
            json={"question": "What is Python?", "limit": 0},
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Limit must be between 1 and 20."
    mock_service.assert_not_called()
