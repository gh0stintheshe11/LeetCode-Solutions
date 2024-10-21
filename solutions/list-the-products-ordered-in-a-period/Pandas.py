import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Filter orders to include only those in February 2020
    feb_orders = orders[(orders['order_date'] >= '2020-02-01') & (orders['order_date'] <= '2020-02-29')]
    
    # Group by product_id and sum the units
    feb_orders_grouped = feb_orders.groupby('product_id', as_index=False)['unit'].sum()
    
    # Filter to include only those with at least 100 units
    feb_orders_filtered = feb_orders_grouped[feb_orders_grouped['unit'] >= 100]
    
    # Merge with products to get product names
    result = pd.merge(feb_orders_filtered, products, on='product_id')
    
    # Select the required columns
    result = result[['product_name', 'unit']]
    
    return result