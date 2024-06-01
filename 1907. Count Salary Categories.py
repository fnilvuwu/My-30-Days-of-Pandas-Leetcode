import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    
    df["category"] = ["Low Salary", "Average Salary", "High Salary"]

    df["accounts_count"] = [sum(accounts["income"]<20000), 
                            sum((accounts["income"]>=20000) & (accounts["income"]<=50000)),
                            sum(accounts["income"]>50000)]
    return df