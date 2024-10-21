import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter rows where the amount is strictly greater than 500
    rich_customers = store[store['amount'] > 500]
    
    # Step 2: Get unique customer_ids
    unique_customers = rich_customers['customer_id'].nunique()
    
    # Step 3: Return the result as a DataFrame with the correct format
    return pd.DataFrame({'rich_count': [unique_customers]})