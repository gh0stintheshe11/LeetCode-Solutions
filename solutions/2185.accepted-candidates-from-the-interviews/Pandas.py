import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Group by interview_id in the Rounds table and calculate the sum of scores for each interview
    interview_scores = rounds.groupby('interview_id')['score'].sum().reset_index()

    # Step 2: Merge the candidates table with the interview_scores table on interview_id
    merged_data = pd.merge(candidates, interview_scores, on='interview_id')

    # Step 3: Filter candidates who have at least 2 years of experience and sum of scores > 15
    result = merged_data[(merged_data['years_of_exp'] >= 2) & (merged_data['score'] > 15)]

    # Step 4: Return only the candidate_id column
    result = result[['candidate_id']]

    return result