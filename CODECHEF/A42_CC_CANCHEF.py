"""
Problem Link :
https://www.codechef.com/problems/CANCHEF
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if (2*y)<=(15*x) else print("NO")