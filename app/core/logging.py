# هذا الملف يضبط نظام التسجيل Logging ليكون موحداً في جميع أجزاء التطبيق.
import logging

def configure_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
