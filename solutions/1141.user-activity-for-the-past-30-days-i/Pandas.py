import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # Define the end date and the start date for the 30-day period
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days=29)
    
    # Convert the activity_date column to datetime
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    
    # Filter the data to include only the last 30 days
    filtered_activity = activity[(activity['activity_date'] >= start_date) & (activity['activity_date'] <= end_date)]
    
    # Group by activity_date and count unique user_id
    daily_active_users = filtered_activity.groupby('activity_date')['user_id'].nunique().reset_index()
    
    # Rename the columns to match the required output format
    daily_active_users.columns = ['day', 'active_users']
    
    return daily_active_users
