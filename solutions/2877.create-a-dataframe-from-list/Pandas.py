import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create a DataFrame from the student_data list with column names 'student_id' and 'age'
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    
    return df