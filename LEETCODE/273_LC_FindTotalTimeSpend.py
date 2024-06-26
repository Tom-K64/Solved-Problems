"""
Problem Link:
https://leetcode.com/problems/find-total-time-spent-by-each-employee/
"""

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    
    result_df = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    
    result_df.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    return result_df
