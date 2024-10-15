import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where any condition starts with "DIAB1"
    diab1_patients = patients[patients['conditions'].str.split().apply(lambda conds: any(c.startswith('DIAB1') for c in conds))]
    
    # Return the result table with the required columns
    return diab1_patients[['patient_id', 'patient_name', 'conditions']]