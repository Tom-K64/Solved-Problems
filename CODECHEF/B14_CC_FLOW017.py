"""
Problem Link :
https://www.codechef.com/problems/FLOW017
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    m=max(a,b,c)
    if a==m:
        print(max(b,c))
    elif b==m:
        print(max(a,c))
    else:
        print(max(a,b))