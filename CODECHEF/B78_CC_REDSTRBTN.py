"""
Problem Link :
https://www.codechef.com/problems/REDSTRBTN
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    c=x+y+z
    if c>=6:
        print("YES")
    else:
        print("NO")