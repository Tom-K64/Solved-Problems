"""
Problem Link :
https://www.codechef.com/problems/T20MCH
"""
r,o,c=map(int,input().split())
rr,ol=r-c,20-o
if rr<(ol*36):
    print("YES")
else:
    print("NO")