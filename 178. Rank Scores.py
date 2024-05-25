import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df_sort_by_scores = scores.sort_values('score', ascending=False)
    # dense method, If there is a tie between two scores, both should have the same value.
    df_sort_by_scores['rank'] = df_sort_by_scores['score'].rank(method='dense', ascending=False).astype(int)

    return df_sort_by_scores[['score', 'rank']]
