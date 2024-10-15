import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Merge signups with confirmations to ensure all users are included
    merged = pd.merge(signups, confirmations, on='user_id', how='left')
    
    # Group by user_id and calculate the number of confirmed and total actions
    grouped = merged.groupby('user_id').agg(
        total_requests=('action', 'count'),
        confirmed_requests=('action', lambda x: (x == 'confirmed').sum())
    ).reset_index()
    
    # Calculate the confirmation rate
    grouped['confirmation_rate'] = grouped['confirmed_requests'] / grouped['total_requests']
    
    # Handle users with no requests by setting their confirmation rate to 0
    grouped['confirmation_rate'] = grouped['confirmation_rate'].fillna(0)
    
    # Round the confirmation rate to two decimal places
    grouped['confirmation_rate'] = grouped['confirmation_rate'].round(2)
    
    # Select the required columns
    result = grouped[['user_id', 'confirmation_rate']]
    
    return result
