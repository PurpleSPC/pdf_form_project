from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
# import re


text = extract_text("test_pdf.pdf")
print(text)

