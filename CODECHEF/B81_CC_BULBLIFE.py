"""
Problem Link :
https://www.codechef.com/problems/BULBLIFE
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    if s>=(n*x):
        print(0)
    else:
        print((n*x)-s)