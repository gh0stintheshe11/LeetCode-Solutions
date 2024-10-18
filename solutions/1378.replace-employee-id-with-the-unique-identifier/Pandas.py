import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join
    result = employees.merge(employee_uni, on='id', how='left')
    
    # Select and rename columns
    result = result[['unique_id', 'name']]
    
    # Sort by name to match the example output
    result = result.sort_values('name')
    
    return result