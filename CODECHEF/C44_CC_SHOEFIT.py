"""
Problem Link :
https://www.codechef.com/problems/SHOEFIT
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (0 in (a,b,c)) and (1 in (a,b,c)):
        print(1)
    else:
        print(0)