"""
Problem Link :
https://www.codechef.com/problems/MILEAGE
"""
t=int(input())
for i in range(t):
    n,x,y,a,b=map(int,input().split())
    mp,md=x/a,y/b
    if (n*mp)<(n*md):
        print("PETROL")
    elif (n*mp)>(n*md):
        print("DIESEL")
    else:
        print("ANY")