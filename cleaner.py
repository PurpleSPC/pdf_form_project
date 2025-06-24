import plumber

# cleaner module
def cleaner(table):
    headers = table[0]
    rows = table[1:]
    
    structured_data = []
    for row in rows:
        # Skip empty rows
        if row == [None] * len(headers):
            continue
        
        # Zip headers and row into a dictionary
        row_dict = dict(zip(headers, row))
        
        # Clean each cell: strip whitespace and remove newlines if it's a string.
        cleaned_dict = {}
        for key, value in row_dict.items():
            if isinstance(value, str):
                cleaned_value = value.strip().replace('\n', ' ')
            else:
                cleaned_value = value
            cleaned_dict[key] = cleaned_value
        
        structured_data.append(cleaned_dict)
    
    return structured_data
