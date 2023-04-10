"""
Problem Link :
https://www.codechef.com/problems/SUBSCRIBE_
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print((int(n/6)+1)*x) if n%6!=0 else print(int(n/6)*x)