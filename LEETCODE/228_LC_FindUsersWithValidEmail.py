"""
Problem Link:
https://leetcode.com/problems/find-users-with-valid-e-mails/
"""
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    
    return valid_emails_df
