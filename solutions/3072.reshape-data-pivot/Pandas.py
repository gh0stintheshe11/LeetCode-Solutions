import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivot the data with 'month' as index and 'city' as columns, values from 'temperature'
    result = weather.pivot(index='month', columns='city', values='temperature')
    
    return result