"""
Problem Link :
https://www.codechef.com/problems/CHEFSLP
"""
t=int(input())
for i in range(t):
    n,l,x=map(int,input().split())
    print(min(l,(n-l))*x)