"""
Problem Link :
https://www.codechef.com/problems/EQLZING
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if abs(a-b)%2==0:
        print("YES")
    else:
        print("NO")