import pdfplumber

def main():

    with pdfplumber.open("test_pdf.pdf") as pdf:
        page = pdf.pages[0]
        tables = page.extract_tables()






main()