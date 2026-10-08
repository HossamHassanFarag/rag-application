# هذا الملف مسؤول عن اختبار API رفع المستندات والتحقق من حالات الملفات غير الصالحة.

from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_upload_unsupported_file_type():

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "test.exe",
                BytesIO(b"some content"),
                "application/octet-stream",
            )
        },
    )

    assert response.status_code == 400
    assert "Unsupported file type" in response.json()["detail"]


def test_upload_empty_file():

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "empty.txt",
                BytesIO(b""),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Uploaded file is empty."
    )


def test_upload_text_file():

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "test.txt",
                BytesIO(
                    b"Python is a programming language."
                ),
                "text/plain",
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "test.txt"
    assert data["chunks_inserted"] > 0
    assert data["status"] == "success"