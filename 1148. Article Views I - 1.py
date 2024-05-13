import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # https://stackoverflow.com/questions/56198775/find-rows-having-same-values-in-multiple-columnsnot-all-columns-in-pandas-data
    unique_views = views[views[['author_id', 'viewer_id']].nunique(axis=1) == 1].drop_duplicates()
    unique_ids = unique_views['author_id'].unique()
    df = pd.DataFrame({'id': unique_ids}).sort_values(by='id')
    return df

