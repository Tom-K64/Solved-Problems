"""
Problem Link:
https://www.codechef.com/problems/M1ENROL
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>=x:
        print(y-x)
    else:
        print(0)