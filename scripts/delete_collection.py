# هذا الملف يحذف مجموعة Qdrant الحالية عند الحاجة لإعادة بناء قاعدة المتجهات.
from app.vector_store.collections import delete_collection
delete_collection()
print("تم حذف المجموعة")
