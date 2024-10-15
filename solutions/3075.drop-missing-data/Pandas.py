import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Drop rows where the 'name' column has missing values (None or NaN)
    result = students.dropna(subset=['name'])
    
    return result