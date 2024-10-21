import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # Merge the project and employee dataframes on employee_id
    merged_df = pd.merge(project, employee, on='employee_id')
    
    # Group by project_id and calculate the average experience_years
    result_df = merged_df.groupby('project_id')['experience_years'].mean().reset_index()
    
    # Rename the columns as required
    result_df.columns = ['project_id', 'average_years']
    
    # Round the average_years to 2 decimal places
    result_df['average_years'] = result_df['average_years'].round(2)
    
    return result_df
