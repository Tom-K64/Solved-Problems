"""
Problem Link:
https://www.codechef.com/problems/POPULATION
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print((x-y)+z)