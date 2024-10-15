import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # Combine requester_id and accepter_id into a single series
    friends = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']])
    
    # Count the number of friends for each user
    friend_counts = friends.value_counts()
    
    # Find the user with the maximum number of friends
    max_friends = friend_counts.max()
    user_with_max_friends = friend_counts.idxmax()
    
    # Prepare the result in the required format
    result = pd.DataFrame({'id': [user_with_max_friends], 'num': [max_friends]})
    
    return result
