import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'grade' column from float to int
    students['grade'] = students['grade'].astype(int)
    
    return students