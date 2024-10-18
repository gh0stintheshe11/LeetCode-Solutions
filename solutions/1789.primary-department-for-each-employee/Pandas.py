import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by employee_id
    grouped = employee.groupby('employee_id')
    
    # Function to find the primary department for each employee
    def get_primary_department(group):
        # Check if there is a primary department
        primary_dept = group[group['primary_flag'] == 'Y']
        if not primary_dept.empty:
            return primary_dept.iloc[0]
        else:
            return group.iloc[0]
    
    # Apply the function to each group and collect the results
    primary_departments = grouped.apply(get_primary_department).reset_index(drop=True)
    
    # Select only the required columns
    result = primary_departments[['employee_id', 'department_id']]
    
    return result
