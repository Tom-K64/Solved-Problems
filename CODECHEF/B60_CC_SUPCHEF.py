"""
Problem Link :
https://www.codechef.com/problems/SUPCHEF
"""
t=int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    if m<=(n*k):
        print("NO")
    else:
        print("YES")