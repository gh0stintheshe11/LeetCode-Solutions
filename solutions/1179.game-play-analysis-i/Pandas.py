import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and find the minimum event_date
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    
    # Rename the column to match the expected output
    result = result.rename(columns={'event_date': 'first_login'})
    
    return result