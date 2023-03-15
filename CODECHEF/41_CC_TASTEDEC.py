"""
Problem Link :
https://www.codechef.com/problems/TASTEDEC
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (2*x) > (5*y):
        print("CHOCOLATE")
    elif (5*y) > (2*x):
        print("CANDY")
    else:
        print("EITHER")