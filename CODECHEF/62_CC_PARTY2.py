"""
Problem Link:
https://www.codechef.com/problems/PARTY2
"""
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    if k<(n*x):
        print("NO")
    else:
        print("YES")