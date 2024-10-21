import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Merge the DataFrame with itself to compare each day's temperature with the previous day's temperature
    weather['previousDate'] = weather['recordDate'] - pd.Timedelta(days=1)
    merged_weather = pd.merge(weather, weather, left_on='previousDate', right_on='recordDate', suffixes=('', '_prev'))
    
    # Filter the rows where the temperature is higher than the previous day's temperature
    rising_temp = merged_weather[merged_weather['temperature'] > merged_weather['temperature_prev']]
    
    # Select the required columns for the output
    result = rising_temp[['id']]
    
    return result
