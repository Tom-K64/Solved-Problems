"""
Problem Link :
https://www.codechef.com/problems/BROKENPHONE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("NEW PHONE") if y<x else print("REPAIR") if x<y else print("ANY")