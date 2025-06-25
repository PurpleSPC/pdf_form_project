import os
import glob
import pdfplumber
 
#processes each pdf and returns the raw extracted tables from pdfplumber 
def process_pdf(pdf_path):
    extracted_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            extracted_tables.extend(tables)
    return extracted_tables

def process_pdf_folder(folder_path):
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    all_records = []

    for file in pdf_files:
        records = process_pdf(file)
        all_records.extend(records)
    
    return all_records

def sort_tables(raw_tables):
    sorted_tables = []
    for table in raw_tables:
        if "Rep ID#" in table[0]:
            rep_table = table
        elif any(item.startswith("Account Name") for item in table[0] if item):
            account_table = table
        elif any(item.startswith("Date") for item in table[0] if item):
            case_table = table
        elif "Catalog #" in table[0]:
            sales_table = table
        elif "Ship To Acct #" in table[0]:
            restock_table = table

    return sorted_tables
