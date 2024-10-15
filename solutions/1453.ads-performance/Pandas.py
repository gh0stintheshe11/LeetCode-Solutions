import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Group by ad_id and action to count clicks and views
    action_counts = ads.groupby(['ad_id', 'action']).size().unstack(fill_value=0)
    
    # Step 2: Ensure all ads are included, even those with no clicks or views
    if 'Clicked' not in action_counts.columns:
        action_counts['Clicked'] = 0
    if 'Viewed' not in action_counts.columns:
        action_counts['Viewed'] = 0

    # Step 3: Calculate CTR for each ad
    action_counts['ctr'] = (action_counts['Clicked'] / (action_counts['Clicked'] + action_counts['Viewed']) * 100).fillna(0)
    
    # Step 4: Reset index to turn ad_id into a column
    result = action_counts.reset_index()[['ad_id', 'ctr']]
    
    # Step 5: Round the CTR to two decimal places
    result['ctr'] = result['ctr'].round(2)
    
    # Step 6: Sort by CTR in descending order and by ad_id in ascending order in case of ties
    result = result.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])
    
    return result