import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # bad time complexity due to the usage of try-catch
    if (N <= 0):
        query = None
        output = pd.DataFrame([[query]], columns=[f"getNthHighestSalary({N})"])
    else:
        df_sort_by_salary = employee.drop_duplicates(subset='salary').sort_values('salary', ascending=False)
        print(df_sort_by_salary)
        try:
            query = df_sort_by_salary.iloc[N - 1].salary
            output = pd.DataFrame([[query]], columns=[f"getNthHighestSalary({N})"])
        except IndexError:
            query = None
            output = pd.DataFrame([[query]], columns=[f"getNthHighestSalary({N})"])
    
    return output