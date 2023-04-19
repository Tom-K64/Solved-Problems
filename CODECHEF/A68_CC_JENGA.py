"""
Problem Link :
https://www.codechef.com/problems/JENGA
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print("YES") if n<=x and x%n==0 else print("NO")