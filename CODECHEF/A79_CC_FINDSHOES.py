"""
Problem Link :
https://www.codechef.com/problems/FINDSHOES
"""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print((n*2)-m) if m<n else print(n)