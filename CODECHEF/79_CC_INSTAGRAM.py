"""
Problem Link :
https://www.codechef.com/problems/INSTAGRAM
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if x>(y*10) else print("NO")