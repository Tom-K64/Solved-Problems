"""
Problem Link :
https://www.codechef.com/problems/TRUESCORE
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    print("POSSIBLE") if a<=c and b<=d else print("IMPOSSIBLE")