import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter employees with salary strictly less than $30,000
    low_salary_employees = employees[employees['salary'] < 30000]
    
    # Step 2: Identify managers who are no longer in the company
    current_employee_ids = set(employees['employee_id'])
    low_salary_employees_with_left_managers = low_salary_employees[
        low_salary_employees['manager_id'].notna() & 
        ~low_salary_employees['manager_id'].isin(current_employee_ids)
    ]
    
    # Step 3: Select only the employee_id column and sort by employee_id
    result = low_salary_employees_with_left_managers[['employee_id']].sort_values(by='employee_id').reset_index(drop=True)
    
    return result