# import the tables from another module
import cleaner

# this code sorts the tables from the cleaner module into their categories

for table in tables:
    if "Rep ID#" in table[0]:
        rep_table = table
    elif "Account Name" in table[0]:
        account_table = table
    elif any(item.startswith("Date") for item in table[0] if item):
        case_table = table
    elif "Catalog #" in table[0]:
        sales_table = table
    elif "Ship To Acct #" in table[0]:
        restock_table = table

print(sales_table[0])
