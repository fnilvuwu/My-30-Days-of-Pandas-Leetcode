import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # it should return 0 or 1 so just multiply by salary
    employees["bonus"] = (
        (employees["employee_id"] % 2 == 1) & (~employees["name"].str.startswith("M"))
    ) * employees["salary"]
    return employees.sort_values(by="employee_id")[["employee_id", "bonus"]]
