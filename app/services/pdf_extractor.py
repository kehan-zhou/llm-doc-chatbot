# app/services/pdf_extractor.py

import pdfplumber
from typing import List

def extract_paragraphs_from_pdf(file_path: str) -> List[str]:
    paragraphs = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                page_paragraphs = [para.strip() for para in text.split("\n") if para.strip()]
                paragraphs.extend(page_paragraphs)

    return paragraphs
