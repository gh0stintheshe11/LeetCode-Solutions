import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate salaries and sort in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there is a second highest salary
    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.iloc[1]
    else:
        second_highest = None
    
    # Return the result as a DataFrame with the correct column name
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})