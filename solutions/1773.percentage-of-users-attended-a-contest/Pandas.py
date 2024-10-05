import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Calculate the total number of users
    total_users = users['user_id'].nunique()
    
    # Step 2: Count the number of unique users registered for each contest
    contest_user_counts = register.groupby('contest_id')['user_id'].nunique().reset_index()
    
    # Step 3: Calculate the percentage of users registered for each contest
    contest_user_counts['percentage'] = (contest_user_counts['user_id'] / total_users) * 100
    
    # Step 4: Round the percentages to two decimal places
    contest_user_counts['percentage'] = contest_user_counts['percentage'].round(2)
    
    # Step 5: Sort the results by percentage in descending order, and by contest_id in ascending order in case of ties
    result = contest_user_counts[['contest_id', 'percentage']].sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    
    return result