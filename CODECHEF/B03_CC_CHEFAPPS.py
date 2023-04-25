"""
Problem Link :
https://www.codechef.com/problems/CHEFAPPS
"""
t=int(input())
for i in range(t):
    s,x,y,z=map(int,input().split())
    l=s-x-y
    if l>=z:
        print(0)
    elif (l+x)>=z or (l+y)>=z:
        print(1)
    else:
        print(2)