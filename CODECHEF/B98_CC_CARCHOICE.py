"""
Problem Link :
https://www.codechef.com/problems/CARCHOICE
"""
t=int(input())
for i in range(t):
    x1,x2,y1,y2=map(int,input().split())
    ex,ey=y1/x1,y2/x2
    print(-1) if ex<ey else print(1) if ey<ex else print(0)