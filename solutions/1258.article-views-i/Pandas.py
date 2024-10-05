import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the author_id is the same as the viewer_id
    result = views[views['author_id'] == views['viewer_id']]
    
    # Select only the unique author_ids and sort them in ascending order
    result = result[['author_id']].drop_duplicates().sort_values(by='author_id')
    
    # Rename the column to 'id' as per the output format
    result.columns = ['id']
    
    return result