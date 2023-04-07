"""
Problem Link :
https://www.codechef.com/problems/COURSEREG
"""
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    print("YES") if m-k>=n else print("NO")