import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Melt the DataFrame to convert store columns into rows
    melted_df = pd.melt(products, id_vars=['product_id'], 
                        value_vars=['store1', 'store2', 'store3'], 
                        var_name='store', value_name='price')
    
    # Filter out rows where price is null
    rearranged_df = melted_df.dropna(subset=['price'])
    
    # Return the rearranged DataFrame
    return rearranged_df[['product_id', 'store', 'price']]