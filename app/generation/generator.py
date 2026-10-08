# هذا الملف مسؤول عن توفير الـ Generator المستخدم حاليًا في تطبيق الـ RAG.

from app.generation.huggingface import HuggingFaceGenerator


def get_generator():
    return HuggingFaceGenerator()