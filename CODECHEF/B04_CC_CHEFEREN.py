"""
Problem Link :
https://www.codechef.com/problems/CHEFEREN
"""
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    e=n//2
    if n%2==0:
        print((e*a)+(e*b))
    else:
        print((e*a)+((e+1)*b))