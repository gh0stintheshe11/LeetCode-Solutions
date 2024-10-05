import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter movies with odd-numbered IDs
    odd_id_movies = cinema[cinema['id'] % 2 != 0]
    
    # Exclude movies with the description "boring"
    not_boring_movies = odd_id_movies[odd_id_movies['description'] != 'boring']
    
    # Sort the result by rating in descending order
    sorted_movies = not_boring_movies.sort_values(by='rating', ascending=False)
    
    return sorted_movies