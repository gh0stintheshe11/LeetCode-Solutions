import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Multiply each salary by 2
    employees['salary'] = employees['salary'] * 2
    
    return employees