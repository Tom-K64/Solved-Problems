"""
Problem Link :
https://www.codechef.com/problems/MARARUN
"""
t=int(input())
for i in range(t):
    D,d,A,B,C=map(int,input().split())
    chef=D*d
    if chef>=10 and chef<21:
        print(A)
    elif chef>=21 and chef<42:
        print(B)
    elif chef>=42:
        print(C)
    else:
        print(0)
        