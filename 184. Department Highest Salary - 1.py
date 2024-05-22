import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))

    max_salary_per_dept = merged.groupby('departmentId')['salary'].max().reset_index()

    result = merged.merge(max_salary_per_dept, on=['departmentId', 'salary'])

    final_result = result[['name_department', 'name_employee', 'salary']].rename(columns={
        'name_department': 'Department',
        'name_employee': 'Employee',
        'salary': 'Salary'
    })

    print(final_result)

    return final_result