import pandas as pd

def restaurant_growth(customers: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Group by visited_on and sum the amount for each day
    daily_totals = customers.groupby('visited_on').agg(amount=('amount', 'sum')).reset_index()
    
    # Step 2: Sort the data by visited_on
    daily_totals = daily_totals.sort_values(by='visited_on')
    
    # Step 3: Calculate the rolling sum and the 7-day moving average
    daily_totals['amount_7_day_sum'] = daily_totals['amount'].rolling(window=7).sum()
    daily_totals['average_amount'] = daily_totals['amount_7_day_sum'] / 7
    
    # Step 4: Round the average_amount to 2 decimal places
    daily_totals['average_amount'] = daily_totals['average_amount'].round(2)
    
    # Step 5: Filter out the rows where the rolling window is not fully populated
    result = daily_totals.dropna(subset=['average_amount'])
    
    # Step 6: Return the result with the appropriate columns
    return result[['visited_on', 'amount_7_day_sum', 'average_amount']].rename(columns={'amount_7_day_sum': 'amount'})