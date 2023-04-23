"""
Problem Link :
https://www.codechef.com/problems/CHEFBOTTLE
"""
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    canfill=k//x
    print(canfill) if canfill<=n else print(n) 