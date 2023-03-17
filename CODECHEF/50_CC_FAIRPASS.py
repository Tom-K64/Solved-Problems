"""
Problem Link:
https://www.codechef.com/problems/FAIRPASS
"""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n<k:
        print("YES")
    else:
        print("NO")