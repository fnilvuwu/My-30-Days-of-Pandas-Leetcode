import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # bad time complexity due to the usage of try-catch
    df_sort_by_salary = employee.drop_duplicates(subset='salary').sort_values('salary', ascending=False)
    print(df_sort_by_salary)
    try:
        query = df_sort_by_salary.iloc[1].salary
        output = pd.DataFrame([[query]], columns=["SecondHighestSalary"])
    except IndexError:
        query = None
        output = pd.DataFrame([[query]], columns=["SecondHighestSalary"])
    
    return output