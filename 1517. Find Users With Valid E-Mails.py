import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # starts with a-zA-Z after that any amount of a-zA-Z0-9._- ends with @leetcode.com
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
    
    valid_users = users[users['mail'].str.contains(pattern, regex=True)]
    
    return valid_users
