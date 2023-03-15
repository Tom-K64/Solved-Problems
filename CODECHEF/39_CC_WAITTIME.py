"""
Problem Link :
https://www.codechef.com/problems/WAITTIME
"""
t=int(input())
for i in range(t):
    k,x=map(int,input().split())
    print((7*k)-x)