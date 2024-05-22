import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = []

    for dept_id in department['id']:
        dept_employees = employee[employee['departmentId'] == dept_id]

        if dept_employees.empty:
            continue

        max_salary = dept_employees['salary'].max()

        highest_paid_employees = dept_employees[dept_employees['salary'] == max_salary]

        for _, row in highest_paid_employees.iterrows():
            result.append({
                'Department': department[department['id'] == dept_id]['name'].values[0],
                'Employee': row['name'],
                'Salary': row['salary']
            })

    if not result:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    result_df = pd.DataFrame(result)

    return result_df
