import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Perform a join operation between sales and product tables on product_id
    merged_df = pd.merge(sales, product, on='product_id')
    
    # Select the required columns
    result_df = merged_df[['product_name', 'year', 'price']]
    
    return result_df