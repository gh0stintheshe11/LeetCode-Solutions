import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    # Corrected regex to match 'bull' and 'bear' when surrounded by spaces
    bull_count = files['content'].str.contains(r'\sbull\s').sum()
    bear_count = files['content'].str.contains(r'\sbear\s').sum()
    
    # Return the result in the required format
    result = pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]
    })
    
    return result