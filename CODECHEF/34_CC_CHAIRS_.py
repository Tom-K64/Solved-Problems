"""
Problem Link :
https://www.codechef.com/problems/CHAIRS_
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<x:
        print(x-y)
    else:
        print(0)