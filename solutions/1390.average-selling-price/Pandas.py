import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Merge the tables on product_id and ensure purchase_date is within the price period
    merged_df = pd.merge(units_sold, prices, on='product_id')
    merged_df = merged_df[(merged_df['purchase_date'] >= merged_df['start_date']) & 
                          (merged_df['purchase_date'] <= merged_df['end_date'])]
    
    # Calculate the total revenue for each sale
    merged_df['revenue'] = merged_df['units'] * merged_df['price']
    
    # Group by product_id to get total revenue and total units sold
    grouped_df = merged_df.groupby('product_id').agg(
        total_revenue=('revenue', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()
    
    # Calculate the average selling price
    grouped_df['average_price'] = grouped_df['total_revenue'] / grouped_df['total_units']
    
    # Round the average price to 2 decimal places
    grouped_df['average_price'] = grouped_df['average_price'].round(2)
    
    # Handle products with no sales
    all_products = pd.DataFrame({'product_id': prices['product_id'].unique()})
    result_df = pd.merge(all_products, grouped_df, on='product_id', how='left')
    result_df['average_price'] = result_df['average_price'].fillna(0)
    
    # Select the required columns
    result_df = result_df[['product_id', 'average_price']]
    
    return result_df