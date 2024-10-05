import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Query to filter products that are both low fat and recyclable
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # Selecting only the product_id column as required
    result = result[['product_id']]
    
    return result