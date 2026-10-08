# هذا الملف هو نقطة تشغيل واجهة Streamlit وتنظيم أقسام تطبيق الـ AI Knowledge Assistant.

import streamlit as st

from frontend.components.chat import render_chat
from frontend.components.sidebar import render_sidebar
from frontend.components.upload import render_upload
from frontend.services.api_client import APIClient


st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
)

api_client = APIClient()

render_sidebar()

st.title("AI Knowledge Assistant")

st.write(
    "Ask questions about your uploaded documents using Retrieval-Augmented Generation."
)

st.divider()

st.header("Documents")

render_upload(api_client)

st.divider()

st.header("Knowledge Assistant")

render_chat(api_client)