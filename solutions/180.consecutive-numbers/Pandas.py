import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Ensure the logs are sorted by id
    logs = logs.sort_values(by='id')
    
    # Create a boolean mask for consecutive numbers
    logs['is_consecutive'] = (logs['num'] == logs['num'].shift(1)) & (logs['num'] == logs['num'].shift(2))
    
    # Filter the logs where the is_consecutive is True
    consecutive_nums = logs[logs['is_consecutive']]['num'].unique()
    
    # Create the result DataFrame
    result = pd.DataFrame(consecutive_nums, columns=['ConsecutiveNums'])
    
    return result
