import pdfplumber
import csv

def main():

    with pdfplumber.open("test_pdf.pdf") as pdf:
        page = pdf.pages[0]
        tables = page.extract_tables()

    for table in tables:
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

    rep_name = cleaner(rep_table[0][0])
    account_name = cleaner(account_table[0][0])
    case_date = cleaner(case_table[0][0])
    surgeon = cleaner(case_table[0][1])
    total_amt = cleaner(restock_table[2][3])
    restock_loc = cleaner(restock_table[0][0])

    data = [
        ["Case Date", "Surgeon", "Account Name", "Rep Name","Billed Amount","Restock Location"],
        [case_date,surgeon,account_name,rep_name,total_amt,restock_loc]
    ]

    with open("output.csv","w",newline=None) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)



def cleaner(field):
    extras = [
        "Account Name",
        "Date",
        "Surgeon (Last, First, MI)",
        "First and Last Name (or Loaner Set ID#)",
        "Name"
    ]
    for extra in extras:
        if field.startswith(extra):
            field = field[len(extra):].strip()
    return field

main()