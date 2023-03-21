"""
Problem Link :
https://www.codechef.com/problems/SIXFRIENDS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (3*x) <= (y*2):
        print(3*x)
    else:
        print(y*2)