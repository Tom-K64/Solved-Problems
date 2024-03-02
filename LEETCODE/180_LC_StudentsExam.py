"""
Problem Link:
https://leetcode.com/problems/students-and-examinations/
"""

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    df1 = students.merge(subjects, how='cross')
    
    df2 = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()
    
    result = df1.merge(df2, on=['student_id','subject_name'], how='left').sort_values(by = ['student_id', 'subject_name'])
    
    return result.fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']]
