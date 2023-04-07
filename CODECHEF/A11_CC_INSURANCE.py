"""
Problem Link :
https://www.codechef.com/problems/INSURANCE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(y) if y<=x else print(x)