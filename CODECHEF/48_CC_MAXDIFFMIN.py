"""
Problem Link:
https://www.codechef.com/problems/MAXDIFFMIN
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(max(x,y,z)-min(x,y,z))