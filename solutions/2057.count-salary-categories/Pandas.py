import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define the salary ranges and count accounts in each category
    low_salary_count = accounts[accounts['income'] < 20000].shape[0]
    average_salary_count = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
    high_salary_count = accounts[accounts['income'] > 50000].shape[0]
    
    # Create and return the result dataframe
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary_count, average_salary_count, high_salary_count]
    })