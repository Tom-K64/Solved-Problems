"""
Problem Link :
https://www.codechef.com/problems/SCALENE
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a!=b and a!=c and b!=c:
        print("YES")
    else:
        print("NO")
    