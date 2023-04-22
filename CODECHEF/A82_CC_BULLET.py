"""
Problem Link :
https://www.codechef.com/problems/BULLET
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if y%x==0:
        sec=y//x
    else:
        sec=(y//x)+1
    print(0) if z<=sec else print(z-sec)