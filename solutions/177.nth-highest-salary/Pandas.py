import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # If N is less than or equal to 0, return null
    if N <= 0:
        nth_salary = None
    else:
        # Remove duplicate salaries and sort in descending order
        unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
        
        # Check if the Nth highest salary exists
        if len(unique_salaries) >= N:
            nth_salary = unique_salaries.iloc[N - 1]
        else:
            nth_salary = None
    
    # Construct the result DataFrame with the correct column name format
    column_name = f'getNthHighestSalary({N})'
    return pd.DataFrame({column_name: [nth_salary]})