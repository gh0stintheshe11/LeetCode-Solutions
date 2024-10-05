import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Identify the first login date for each player
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id', 'first_login_date']
    
    # Step 2: Merge the first login date back to the original activity table
    activity = activity.merge(first_login, on='player_id')
    
    # Step 3: Calculate the day after the first login date
    activity['next_day'] = activity['first_login_date'] + pd.Timedelta(days=1)
    
    # Step 4: Check if the player logged in on the next day
    next_day_login = activity[activity['event_date'] == activity['next_day']]
    
    # Step 5: Get the unique player_ids who logged in on the next day
    players_next_day_login = next_day_login['player_id'].nunique()
    
    # Step 6: Get the total number of unique players
    total_players = activity['player_id'].nunique()
    
    # Step 7: Calculate the fraction and round to 2 decimal places
    fraction = round(players_next_day_login / total_players, 2)
    
    # Step 8: Create the result DataFrame
    result = pd.DataFrame({'fraction': [fraction]})
    
    return result
