import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    nth_highest = sorted_salaries.iloc[N - 1]
    return pd.DataFrame({'Nth Highest Salary': [nth_highest]})
"""
Problem Link:
https://leetcode.com/problems/nth-highest-salary/
"""
