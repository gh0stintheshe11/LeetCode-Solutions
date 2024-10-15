import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Identify the first order for each customer
    first_orders = delivery.loc[delivery.groupby('customer_id')['order_date'].idxmin()]
    
    # Step 2: Determine if each first order is immediate or scheduled
    first_orders['is_immediate'] = first_orders['order_date'] == first_orders['customer_pref_delivery_date']
    
    # Step 3: Calculate the percentage of immediate first orders
    immediate_count = first_orders['is_immediate'].sum()
    total_count = first_orders.shape[0]
    immediate_percentage = (immediate_count / total_count) * 100
    
    # Step 4: Format the result to two decimal places
    result = pd.DataFrame({'immediate_percentage': [round(immediate_percentage, 2)]})
    
    return result
