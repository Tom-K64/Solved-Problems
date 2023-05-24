"""
Problem Link :
https://www.codechef.com/problems/CCISLAND
"""
t=int(input())
for i in range(t):
    x,y,xr,yr,d=map(int,input().split())
    r=min(x/xr,y/yr)
    if r>=d:
        print("YES")
    else:
        print("NO")