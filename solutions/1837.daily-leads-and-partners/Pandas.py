import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by date_id and make_name, then count unique lead_id's and partner_id's
    result = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': 'nunique',
        'partner_id': 'nunique'
    }).reset_index()
    
    # Rename the columns to match the expected output
    result = result.rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners'
    })
    
    return result