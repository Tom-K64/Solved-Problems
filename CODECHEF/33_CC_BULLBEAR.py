"""
Problem Link :
https://www.codechef.com/problems/BULLBEAR
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>x:
        print("PROFIT")
    elif y<x:
        print("LOSS")
    else:
        print("NEUTRAL")