import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the total number of unique products
    total_products = product['product_key'].nunique()
    
    # Step 2: Count the number of unique products each customer has purchased
    customer_product_count = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    
    # Step 3: Filter customers who have purchased all products
    customers_who_bought_all = customer_product_count[customer_product_count['product_key'] == total_products]
    
    # Select only the customer_id column for the result
    result = customers_who_bought_all[['customer_id']]
    
    return result
