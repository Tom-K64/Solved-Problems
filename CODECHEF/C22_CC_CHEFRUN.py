"""
Problem Link :
https://www.codechef.com/problems/CHEFRUN
"""
t=int(input())
for i in range(t):
    x1,x2,x3,v1,v2=map(int,input().split())
    s1,s2=(x3-x1)/v1,(x2-x3)/v2
    if s1>s2:
        print("Kefa")
    elif s2>s1:
        print("Chef")
    else:
        print("Draw")