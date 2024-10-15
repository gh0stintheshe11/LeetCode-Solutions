import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the scores in descending order
    scores_sorted = scores.sort_values(by='score', ascending=False)
    
    # Rank the scores with no gaps between ranks, ties have the same rank
    scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)
    
    # Return the sorted dataframe with score and rank columns
    return scores_sorted[['score', 'rank']]