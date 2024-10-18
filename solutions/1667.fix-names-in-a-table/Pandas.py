import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Apply str.capitalize() to the 'name' column to fix the names
    users['name'] = users['name'].str.capitalize()
    
    # Return the result ordered by user_id
    return users.sort_values(by='user_id')