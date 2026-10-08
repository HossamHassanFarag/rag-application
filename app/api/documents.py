# هذا الملف مسؤول عن استقبال المستندات والتحقق منها ثم إرسالها إلى خدمة الـ Ingestion وتخزينها في Qdrant.

from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.documents.service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

MAX_FILE_SIZE = 200 * 1024 * 1024


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
):
    allowed_extensions = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
    }

    filename = file.filename or ""
    extension = Path(filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension or 'unknown'}",
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty.",
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Uploaded file exceeds the 200 MB limit.",
        )

    temp_path = None

    try:
        with NamedTemporaryFile(
            delete=False,
            suffix=extension,
        ) as temp_file:
            temp_file.write(content)
            temp_path = temp_file.name

        count = DocumentService().ingest(
            temp_path,
            source_name=filename,
        )

        if count == 0:
            raise HTTPException(
                status_code=400,
                detail="No readable text was found in the document.",
            )

        return {
            "filename": filename,
            "chunks_inserted": count,
            "status": "success",
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Document processing failed.",
        )

    finally:
        if temp_path:
            Path(temp_path).unlink(
                missing_ok=True
            )