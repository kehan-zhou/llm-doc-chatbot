# app/routes/upload.py

from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.pdf_extractor import extract_paragraphs_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    paragraphs = extract_paragraphs_from_pdf(file_location)

    return {
        "filename": file.filename,
        "paragraphs": paragraphs,
        "message": "File uploaded and text extracted successfully"
    }
