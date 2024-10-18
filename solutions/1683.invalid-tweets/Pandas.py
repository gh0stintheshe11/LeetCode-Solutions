import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the length of the content is greater than 15
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]
    
    # Return only the tweet_id column
    return invalid_tweets_df[['tweet_id']]