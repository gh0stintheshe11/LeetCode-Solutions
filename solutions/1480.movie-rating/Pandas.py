import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the user who has rated the greatest number of movies
    user_ratings_count = movie_rating.groupby('user_id').size().reset_index(name='rating_count')
    max_ratings = user_ratings_count['rating_count'].max()
    top_users = user_ratings_count[user_ratings_count['rating_count'] == max_ratings]
    top_users = top_users.merge(users, on='user_id')
    top_user_name = top_users['name'].min()
    
    # Step 2: Find the movie with the highest average rating in February 2020
    feb_ratings = movie_rating[(movie_rating['created_at'] >= '2020-02-01') & (movie_rating['created_at'] <= '2020-02-29')]
    movie_avg_ratings = feb_ratings.groupby('movie_id')['rating'].mean().reset_index(name='avg_rating')
    max_avg_rating = movie_avg_ratings['avg_rating'].max()
    top_movies = movie_avg_ratings[movie_avg_ratings['avg_rating'] == max_avg_rating]
    top_movies = top_movies.merge(movies, on='movie_id')
    top_movie_title = top_movies['title'].min()
    
    # Prepare the result
    result = pd.DataFrame({'results': [top_user_name, top_movie_title]})
    return result
