import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Count the occurrences of each number
    counts = my_numbers['num'].value_counts()
    
    # Filter out numbers that appear more than once
    single_numbers = counts[counts == 1].index
    
    # Find the maximum single number
    if len(single_numbers) == 0:
        result = pd.DataFrame({'num': [None]})
    else:
        max_single_number = max(single_numbers)
        result = pd.DataFrame({'num': [max_single_number]})
    
    return result
