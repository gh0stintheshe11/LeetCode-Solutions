import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # Sort the queue by the 'turn' column to process people in the correct order
    queue = queue.sort_values(by='turn')
    
    # Initialize the total weight on the bus
    total_weight = 0
    
    # Iterate through the sorted queue
    for index, row in queue.iterrows():
        # Check if adding this person's weight would exceed the limit
        if total_weight + row['weight'] > 1000:
            # If it exceeds, return the name of the last person who successfully boarded
            return pd.DataFrame({'person_name': [last_person_name]})
        
        # Update the total weight and the last person's name
        total_weight += row['weight']
        last_person_name = row['person_name']
    
    # If all people can board without exceeding the limit, return the last person's name
    return pd.DataFrame({'person_name': [last_person_name]})