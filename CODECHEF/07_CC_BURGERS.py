"""
Problem Link :
https://www.codechef.com/problems/BURGERS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<=y:
        print(x)
    elif y<=x:
        print(y)