import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Cross join Students and Subjects
    cross_join = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)
    
    # Group Examinations and count occurrences
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    # Merge cross join with exam counts
    result = cross_join.merge(exam_counts, on=['student_id', 'subject_name'], how='left')
    
    # Fill NaN values with 0 for students who didn't attend exams
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    
    # Sort the result
    result = result.sort_values(['student_id', 'subject_name'])
    
    # Select and reorder columns
    result = result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    
    return result