import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # Define the target date
    target_date = pd.to_datetime('2019-08-16')
    
    # Filter the products to include only those changes on or before the target date
    filtered_products = products[products['change_date'] <= target_date]
    
    # Sort the filtered products by product_id and change_date in descending order
    filtered_products = filtered_products.sort_values(by=['product_id', 'change_date'], ascending=[True, False])
    
    # Drop duplicates to keep only the latest price change for each product
    latest_prices = filtered_products.drop_duplicates(subset=['product_id'], keep='first')
    
    # Create a DataFrame with all unique product_ids
    all_products = pd.DataFrame({'product_id': products['product_id'].unique()})
    
    # Merge with the latest prices to get the price on the target date
    result = all_products.merge(latest_prices[['product_id', 'new_price']], on='product_id', how='left')
    
    # Fill NaN values with the default price of 10
    result['new_price'] = result['new_price'].fillna(10).astype(int)
    
    # Rename the columns to match the expected output
    result = result.rename(columns={'new_price': 'price'})
    
    return result
