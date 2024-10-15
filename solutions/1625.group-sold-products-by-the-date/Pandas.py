import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Sort the dataframe by sell_date and product
    activities = activities.sort_values(['sell_date', 'product'])
    
    # Count unique products per date
    activities['num_sold'] = activities.groupby('sell_date')['product'].transform('nunique')
    
    # Group by sell_date and aggregate
    result = activities.groupby('sell_date').agg({
        'product': lambda x: ','.join(sorted(set(x))),
        'num_sold': 'first'
    }).reset_index()
    
    # Rename the 'product' column to 'products'
    result = result.rename(columns={'product': 'products'})
    
    # Ensure num_sold is of integer type
    result['num_sold'] = result['num_sold'].astype(int)
    
    # Reorder columns to match expected output
    result = result[['sell_date', 'num_sold', 'products']]
    
    return result