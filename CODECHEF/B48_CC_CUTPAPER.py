"""
Problem Link :
https://www.codechef.com/problems/CUTPAPER
"""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    print((n//k)*(n//k))