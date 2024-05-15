import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    cond = tweets["content"].str.len() > 15
    # this will query the condition and then create a new df with only the column tweet_id
    result = tweets[cond][["tweet_id"]]
    print(result)
    return result