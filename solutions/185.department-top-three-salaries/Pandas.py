import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the employee and department tables on departmentId and id
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # Sort the merged DataFrame by departmentId and salary in descending order
    merged_df = merged_df.sort_values(by=['departmentId', 'salary'], ascending=[True, False])
    
    # Group by departmentId and department name
    grouped = merged_df.groupby(['departmentId', 'name_dept'])
    
    # Function to get top three unique salaries
    def get_top_three(group):
        # Get the unique salaries in descending order
        unique_salaries = group['salary'].unique()
        top_three_salaries = unique_salaries[:3]
        
        # Filter the group to only include employees with one of the top three salaries
        return group[group['salary'].isin(top_three_salaries)]
    
    # Apply the function to each group and reset the index
    result_df = grouped.apply(get_top_three).reset_index(drop=True)
    
    # Select the required columns and rename them
    result_df = result_df[['name_dept', 'name_emp', 'salary']]
    result_df.columns = ['Department', 'Employee', 'Salary']
    
    return result_df
