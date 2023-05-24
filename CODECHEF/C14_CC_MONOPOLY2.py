"""
Problem Link :
https://www.codechef.com/problems/MONOPOLY2
"""
t=int(input())
for i in range(t):
    p,q,r,s=map(int,input().split())
    m=max(p,q,r,s)
    if m>(p+q+r+s-m):
        print("YES")
    else:
        print("NO")