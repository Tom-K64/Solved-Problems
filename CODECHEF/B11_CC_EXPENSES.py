"""
Problem Link :
https://www.codechef.com/problems/EXPENSES
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    income=2**x
    for i in range(1,n+1):
        income=income//2
    print(income)