import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    cond = (world["area"] >= 3000000) | (world["population"] >= 25000000)
    result = world[cond]
    return result[["name", "population", "area"]]
        