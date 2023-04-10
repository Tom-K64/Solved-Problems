"""
Problem Link :
https://www.codechef.com/problems/CGYM
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(2) if z>=(x+y) else print(1) if z>=x else print(0)