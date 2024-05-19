import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # check if any word start with DIAB1
    cond = patients["conditions"].str.contains(r'(^|\s)DIAB1')
    result = patients[cond]
    return result