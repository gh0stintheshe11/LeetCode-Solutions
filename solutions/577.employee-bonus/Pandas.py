import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join between employee and bonus tables on empId
    merged_df = pd.merge(employee, bonus, on='empId', how='left')
    
    # Filter the rows where bonus is less than 1000 or is null
    result_df = merged_df[(merged_df['bonus'] < 1000) | (merged_df['bonus'].isnull())]
    
    # Select only the name and bonus columns for the result
    result_df = result_df[['name', 'bonus']]
    
    return result_df
