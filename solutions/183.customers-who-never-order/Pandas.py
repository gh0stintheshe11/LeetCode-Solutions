import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Find the customers who are not in the orders table by using a left join
    result = customers[~customers['id'].isin(orders['customerId'])][['name']]
    
    # Rename the column to 'Customers' as per the required output
    result.columns = ['Customers']
    
    return result