import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate time spent for each entry
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    
    # Group by emp_id and event_day, sum up time_spent
    result = employees.groupby(['event_day', 'emp_id'])['time_spent'].sum().reset_index()
    
    # Rename columns to match expected output
    result = result.rename(columns={
        'event_day': 'day',
        'time_spent': 'total_time'
    })
    
    # Reorder columns to match expected output
    result = result[['day', 'emp_id', 'total_time']]
    
    return result