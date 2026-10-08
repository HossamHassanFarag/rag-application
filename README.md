# AI Knowledge Assistant

مشروع RAG مقسم إلى FastAPI وStreamlit وQdrant وSentence Transformers وOllama.

## التشغيل

1. ثبّت المتطلبات: `python -m pip install -r requirements.txt`
2. شغّل Qdrant محلياً.
3. شغّل Ollama وحمّل النموذج الموجود في `.env`.
4. شغّل الـ API: `uvicorn app.main:app --reload`
5. شغّل الواجهة: `streamlit run frontend/streamlit_app.py`
