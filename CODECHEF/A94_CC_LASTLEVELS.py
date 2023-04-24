"""
Problem Link :
https://www.codechef.com/problems/LASTLEVELS
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x%3==0 :
        br=(x//3) -1
    else:
        br=x//3
    print((x*y)+(z*br))