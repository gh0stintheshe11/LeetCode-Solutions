import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the DataFrame by 'id' in ascending order so that the smallest id comes first
    person.sort_values(by='id', inplace=True)
    
    # Keep only the first occurrence of each email and drop the others
    person.drop_duplicates(subset='email', keep='first', inplace=True)