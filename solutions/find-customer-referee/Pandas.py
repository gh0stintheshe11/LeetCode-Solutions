import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter customers whose referee_id is not 2 (including those with null referee_id)
    result = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]
    
    # Return only the 'name' column
    return result[['name']]