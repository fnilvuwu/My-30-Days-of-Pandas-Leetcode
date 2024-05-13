import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # https://stackoverflow.com/questions/61964973/pandas-get-column-value-where-row-matches-condition
    cond = (world["area"] >= 3000000) | (world["population"] >= 25000000)
    result = world[cond]
    return result[["name", "population", "area"]]
        