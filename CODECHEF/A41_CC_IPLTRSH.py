"""
Problem Link :
https://www.codechef.com/problems/IPLTRSH
"""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(n-m) if n>m else print(0)