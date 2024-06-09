import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first_login"] = activity.groupby('player_id')['event_date'].transform('min')
    activity = activity.dropna(subset=['first_login'])[['player_id', 'first_login']].drop_duplicates()
    return activity