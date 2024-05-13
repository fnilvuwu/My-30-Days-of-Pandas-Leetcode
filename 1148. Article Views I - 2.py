import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    author_viewer = views[views['author_id'] == views['viewer_id']]
    unique_author_id = sorted(author_viewer['author_id'].unique())
    output = pd.DataFrame(unique_author_id,columns=['id'])
    return output