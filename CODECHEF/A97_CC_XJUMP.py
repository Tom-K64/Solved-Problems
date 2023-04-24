"""
Problem Link :
https://www.codechef.com/problems/XJUMP
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print((x//y)+(x%y))