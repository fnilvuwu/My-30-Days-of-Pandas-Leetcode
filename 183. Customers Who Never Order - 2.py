import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html
    df = customers[~customers['id'].isin(orders['customerId'])]
    df = df[['name']].rename(columns={'name':'Customers'})
    return df