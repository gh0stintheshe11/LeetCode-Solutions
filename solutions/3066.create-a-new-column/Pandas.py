import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' by doubling the 'salary' column
    employees['bonus'] = employees['salary'] * 2
    
    return employees