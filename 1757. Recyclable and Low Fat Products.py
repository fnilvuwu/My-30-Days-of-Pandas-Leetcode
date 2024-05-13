import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    cond = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    result = products[cond]
    return result[["product_id"]]