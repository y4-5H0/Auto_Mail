import pandas as pd

# Use pandas to read the Excel file and extract emails.
def get_email_list(file_path):
    df = pd.read_excel(file_path)
    return df['Email'].dropna().tolist()