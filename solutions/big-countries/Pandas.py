import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter countries that have either area >= 3000000 or population >= 25000000
    result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Select only the name, population, and area columns
    result = result[['name', 'population', 'area']]
    
    return result