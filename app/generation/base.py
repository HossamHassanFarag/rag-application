# هذا الملف يحدد الواجهة الأساسية لأي مزود لنموذج اللغة داخل المشروع.

from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        pass