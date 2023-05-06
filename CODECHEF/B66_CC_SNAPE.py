"""
Problem Link :
https://www.codechef.com/problems/SNAPE
"""
from math import sqrt
t=int(input())
for i in range(t):
    b,h=map(int,input().split())
    print("%.5f"%(sqrt((h**2)-(b**2))),"%.5f"%(sqrt((b**2)+(h**2))))
    