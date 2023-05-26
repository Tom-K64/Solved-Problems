"""
Problem Link :
https://www.codechef.com/problems/UTKPLC
"""
t=int(input())
for i in range(t):
    f,s,t=map(str,input().split())
    x,y=map(str,input().split())
    if f in (x,y):
        print(f)
    elif s in (x,y):
        print(s)
    else:
        print(t)
    