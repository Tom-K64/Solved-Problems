"""
Problem Link :
https://www.codechef.com/problems/RECTSQ
"""
from math import gcd
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    s=gcd(n,m)
    print((n*m)//(s*s))