import pandas as pd

# Define a lambda function to round the values to 2 decimal places
round2 = lambda x: round(x + 1e-9, 2)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Calculate the quality as (rating / position) for each row
    queries['quality'] = queries['rating'] / queries['position']
    
    # Step 2: Calculate poor query percentage (where rating < 3), multiplying by 100 to convert to percentage
    queries['poor_query_percentage'] = (queries['rating'] < 3) * 100
    
    # Step 3: Group by 'query_name' and compute the mean of both columns, then apply rounding
    result = queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().apply(round2).reset_index()
    
    return result