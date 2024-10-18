import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter for immediate orders
    immediate_orders = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    
    # Step 2: Calculate the percentage of immediate orders
    immediate_percentage = (len(immediate_orders) / len(delivery)) * 100
    
    # Step 3: Round the result to 2 decimal places
    immediate_percentage = round(immediate_percentage, 2)
    
    # Step 4: Return the result as a DataFrame
    return pd.DataFrame({'immediate_percentage': [immediate_percentage]})