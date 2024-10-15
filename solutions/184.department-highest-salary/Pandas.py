import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the employee and department data on departmentId and department id
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    
    # Group by department and find the maximum salary in each department
    max_salaries = merged_df.groupby('name_department')['salary'].transform('max')
    
    # Filter the employees who have the maximum salary in their respective departments
    result_df = merged_df[merged_df['salary'] == max_salaries]
    
    # Select the required columns and rename them
    result_df = result_df[['name_department', 'name_employee', 'salary']].rename(columns={
        'name_department': 'Department',
        'name_employee': 'Employee',
        'salary': 'Salary'
    })
    
    return result_df