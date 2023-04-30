"""
Problem Link :
https://www.codechef.com/problems/BUYLAMP
"""
t=int(input())
for i in range(t):
    n,k,x,y=map(int,input().split())
    cost=k*x
    n-=k
    if x<=y:
        cost+=(n*x)
    else:
        cost+=(n*y)
    print(cost)