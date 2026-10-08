# هذا الملف يوفر دوال اختيارية لتصفية نتائج الاسترجاع حسب Metadata.
def filter_results(results, filename=None):
    if not filename: return results
    return [r for r in results if (r.payload or {}).get("filename") == filename]
