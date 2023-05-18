"""
Problem Link :
https://www.codechef.com/problems/FLOW009
"""
t=int(input())
for i in range(t):
    q,p=map(int,input().split())
    s=q*p
    if q>1000:
        print(s*0.9)
    else:
        print(s*1.0)