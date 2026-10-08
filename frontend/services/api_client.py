# هذا الملف مسؤول عن التواصل بين واجهة Streamlit وواجهة FastAPI.

import requests


class APIClient:

    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")

    def upload_document(self, file_name: str, file_bytes: bytes):
        response = requests.post(
            f"{self.base_url}/documents/upload",
            files={
                "file": (
                    file_name,
                    file_bytes,
                )
            },
        )

        response.raise_for_status()

        return response.json()

    def query(
        self,
        question: str,
        limit: int = 5,
    ):
        response = requests.post(
            f"{self.base_url}/query",
            json={
                "question": question,
                "limit": limit,
            },
        )

        response.raise_for_status()

        return response.json()

    def health(self):
        response = requests.get(
            f"{self.base_url}/health"
        )

        response.raise_for_status()

        return response.json()