"""
Problem Link :
https://www.codechef.com/problems/DISTINCTCOL
"""
t=int(input())
for i in range(t):
    n=int(input())
    col=list(map(int,input().split()))
    print(max(col))