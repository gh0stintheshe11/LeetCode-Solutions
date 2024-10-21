import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # Iterate over the DataFrame in steps of 2
    for i in range(0, len(seat) - 1, 2):
        # Swap the 'student' values of the current row and the next row
        seat.at[i, 'student'], seat.at[i + 1, 'student'] = seat.at[i + 1, 'student'], seat.at[i, 'student']
    
    return seat
