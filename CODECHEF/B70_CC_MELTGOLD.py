"""
Problem Link :
https://www.codechef.com/problems/MELTGOLD
"""
from math import sqrt
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(round(sqrt(2*(x-y))))