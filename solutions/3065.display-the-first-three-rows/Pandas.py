import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use the head function to get the first 3 rows of the DataFrame
    return employees.head(3)