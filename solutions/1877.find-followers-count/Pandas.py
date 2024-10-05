import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # Group by user_id and count the number of followers for each user
    result = followers.groupby('user_id').size().reset_index(name='followers_count')
    
    # Sort the result by user_id in ascending order
    result = result.sort_values(by='user_id').reset_index(drop=True)
    
    return result
