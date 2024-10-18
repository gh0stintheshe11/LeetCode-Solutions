import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id, count collaborations
    collaborations = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
    # Filter for pairs with at least 3 collaborations
    result = collaborations[collaborations['count'] >= 3][['actor_id', 'director_id']]
    
    return result