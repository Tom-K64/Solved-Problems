"""
Problem Link :
https://www.codechef.com/problems/MONOPOLY
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print("YES") if x>(y+z) or y>(x+z) or z>(x+y) else print("NO")