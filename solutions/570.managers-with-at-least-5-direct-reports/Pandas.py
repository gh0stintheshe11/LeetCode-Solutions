import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by managerId and count the number of direct reports (employees) for each manager
    report_counts = employee.groupby('managerId')['id'].count().reset_index()
    
    # Filter to find managers with at least 5 direct reports
    managers_with_5_or_more_reports = report_counts[report_counts['id'] >= 5]
    
    # Merge the result with the employee table to get the manager names
    result = pd.merge(managers_with_5_or_more_reports, employee, left_on='managerId', right_on='id', how='inner')
    
    # Select only the 'name' column and return it
    return result[['name']]