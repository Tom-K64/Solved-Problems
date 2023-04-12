"""
Problem Link :
https://www.codechef.com/problems/MINPIZZA
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if (n*x)%4==0:
        print(int((n*x)/4))
    else:
        print(int((n*x)/4)+1)