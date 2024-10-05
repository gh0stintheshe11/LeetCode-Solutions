import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Rename the columns using the rename method
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })
    
    return students