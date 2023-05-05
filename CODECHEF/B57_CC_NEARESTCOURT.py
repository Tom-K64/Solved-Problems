"""
Problem Link :
https://www.codechef.com/problems/NEARESTCOURT
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=abs(x-y)
    if z%2==0:
        print(z//2)
    else:
        print((z//2)+1)