# هذا الملف يحفظ بيانات المستندات الوصفية بشكل بسيط ويمكن استبداله بقاعدة بيانات لاحقاً.
class DocumentRepository:
    def __init__(self): self.documents=[]
    def add(self, item): self.documents.append(item); return item
    def list(self): return self.documents
