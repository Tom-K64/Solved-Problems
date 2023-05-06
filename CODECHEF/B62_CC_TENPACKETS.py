"""
Problem Link :
https://www.codechef.com/problems/TENPACKETS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<(2*x):
        print(y+y+x)
    else:
        print(5*x)