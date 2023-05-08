"""
Problem Link :
https://www.codechef.com/problems/OPMIN
"""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=a.count(min(a))
    if x<=1:
        print(n-1)
    else:
        print(n-1-(x-1))