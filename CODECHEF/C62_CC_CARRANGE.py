"""
Problem Link :
https://www.codechef.com/problems/CARRANGE
"""
t=int(input())
for i in range(t):
    p,m,v=map(int,input().split())
    print((m-p+1)*v)