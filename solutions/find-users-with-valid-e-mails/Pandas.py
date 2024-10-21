import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define the regular expression for a valid email
    valid_email_regex = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
    
    # Filter the users whose mail matches the regular expression
    valid_users = users[users['mail'].str.match(valid_email_regex)]
    
    # Return the valid users
    return valid_users[['user_id', 'name', 'mail']]