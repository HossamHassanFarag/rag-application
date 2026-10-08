# هذا الملف يختبر تنظيف النصوص وإزالة الفراغات الزائدة.
from app.ingestion.cleaner import clean_text
def test_clean_text(): assert clean_text(" a  \n\n b ") == "a\n\nb"
