"""
Problem Link :
https://www.codechef.com/problems/AIRLINES
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(y*z) if y<=(x*10) else print(x*10*z)
        