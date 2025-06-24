from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import re


text = extract_text("test_pdf.pdf")
lines = text.splitlines()
chunks = [line.strip() for line in lines if line.strip()]

for chunk in chunks:
    print(chunk)

