"""
Problem Link :
https://www.codechef.com/problems/RIGHTTHERE
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print("YES") if n<=x else print("NO")