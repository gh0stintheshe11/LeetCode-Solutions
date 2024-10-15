import pandas as pd
import math

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Identify the employees who have direct reports by filtering where reports_to is not null
    reports = employees[employees['reports_to'].notna()]
    
    # Step 2: Group by 'reports_to' to calculate the number of direct reports and the average age of reports
    report_stats = reports.groupby('reports_to').agg(
        reports_count=('employee_id', 'size'),   # Count the number of direct reports
        average_age=('age', 'mean')              # Calculate the average age of direct reports
    ).reset_index()
    
    # Step 3: Custom rounding of average age to ensure proper rounding behavior
    report_stats['average_age'] = report_stats['average_age'].apply(lambda x: math.ceil(x) if x - int(x) == 0.5 else round(x))
    
    # Step 4: Merge with the original employees DataFrame to get the manager's name
    result = report_stats.merge(employees, left_on='reports_to', right_on='employee_id')
    
    # Step 5: Select the required columns and rename them
    result = result[['employee_id', 'name', 'reports_count', 'average_age']]
    
    # Step 6: Sort the result by employee_id
    result = result.sort_values(by='employee_id').reset_index(drop=True)
    
    return result