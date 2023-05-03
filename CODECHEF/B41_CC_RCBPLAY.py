"""
Problem Link :
https://www.codechef.com/problems/RCBPLAY
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (x+(z*2))>=y:
        print("YES")
    else:
        print("NO")