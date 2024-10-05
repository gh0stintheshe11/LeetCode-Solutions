import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the bonus based on the conditions
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if (row['employee_id'] % 2 != 0 and not row['name'].startswith('M')) else 0, axis=1
    )
    
    # Return the result ordered by employee_id
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')