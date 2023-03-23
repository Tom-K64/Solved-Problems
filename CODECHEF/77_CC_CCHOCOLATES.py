"""
Problem Link :
https://www.codechef.com/problems/CCHOCOLATES
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    Rs=(x*5)+(y*10)
    print(int(Rs/z))