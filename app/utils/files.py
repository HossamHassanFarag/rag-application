# هذا الملف يحتوي على أدوات عامة للتعامل مع أسماء الملفات وامتداداتها.
from pathlib import Path
def extension(filename: str) -> str: return Path(filename).suffix.lower()
