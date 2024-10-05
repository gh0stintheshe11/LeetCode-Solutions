import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter the row where student_id is 101 and select only the 'name' and 'age' columns
    result = students[students['student_id'] == 101][['name', 'age']]
    
    return result