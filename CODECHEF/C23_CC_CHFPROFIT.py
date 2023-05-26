"""
Problem Link :
https://www.codechef.com/problems/CHFPROFIT
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print((x*z)-(x*y))