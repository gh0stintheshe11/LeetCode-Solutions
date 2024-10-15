import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count orders
    order_counts = orders.groupby('customer_number').size().reset_index(name='order_count')
    
    # Find the customer(s) with the maximum number of orders
    max_orders = order_counts['order_count'].max()
    result = order_counts[order_counts['order_count'] == max_orders][['customer_number']]
    
    return result