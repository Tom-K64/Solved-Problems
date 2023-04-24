"""
Problem Link :
https://www.codechef.com/problems/WGHTS
"""
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if (x+y)==w or (y+z)==w or (x+z)==w or(x+y+z)==w or x==w or y==w or z==w:
        print("YES")
    else:
        print("NO")