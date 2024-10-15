import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate rows based on the 'email' column, keeping only the first occurrence
    result = customers.drop_duplicates(subset=['email'], keep='first')
    
    return result