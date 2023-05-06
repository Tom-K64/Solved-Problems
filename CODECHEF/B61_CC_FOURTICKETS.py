"""
Problem Link :
https://www.codechef.com/problems/FOURTICKETS
"""
t=int(input())
for i in range(t):
    x=int(input())
    print("YES") if 1000>=(x*4) else print("NO")