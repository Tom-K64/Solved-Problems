"""
Problem Link :
https://www.codechef.com/problems/WATERFLOW
"""
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    water=w+(y*z)
    print("OVERFLOW") if water>x else print("FILLED") if water==x else print("UNFILLED")