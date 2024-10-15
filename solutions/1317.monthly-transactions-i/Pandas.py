import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # Ensure trans_date is in datetime format
    transactions['trans_date'] = pd.to_datetime(transactions['trans_date'])
    
    # Extract the month from the trans_date column
    transactions['month'] = transactions['trans_date'].dt.to_period('M').astype(str)
    
    # Group by month and country (including null values in the country)
    grouped = transactions.groupby(['month', 'country'], dropna=False)
    
    # Calculate the required metrics
    result = grouped.agg(
        trans_count=('id', 'count'),
        trans_total_amount=('amount', 'sum'),
        approved_count=('state', lambda x: (x == 'approved').sum()),
        approved_total_amount=('amount', lambda x: x[transactions['state'] == 'approved'].sum())
    ).reset_index()
    
    # Rearrange the column order to match the expected output
    result = result[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]
    
    return result