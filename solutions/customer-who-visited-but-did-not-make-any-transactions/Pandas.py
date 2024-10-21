import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Identify visits without transactions
    visits_with_transactions = transactions['visit_id'].unique()
    visits_without_transactions = visits[~visits['visit_id'].isin(visits_with_transactions)]
    
    # Step 2: Count the number of visits without transactions per customer
    result = visits_without_transactions.groupby('customer_id').size().reset_index(name='count_no_trans')
    
    # Step 3: Return the result
    return result
