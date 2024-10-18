import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and count unique subject_id's
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    
    # Rename the count column to 'cnt'
    result = result.rename(columns={'subject_id': 'cnt'})
    
    return result