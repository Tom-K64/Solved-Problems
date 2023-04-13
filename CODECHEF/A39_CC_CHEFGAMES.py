"""
Problem Link :
https://www.codechef.com/problems/CHEFGAMES
"""
t=int(input())
for i in range(t):
    r1,r2,r3,r4=map(int,input().split())
    if r1==r2 and r2==r3 and r3==r4:
        if r1==0:
            print("IN")
        else:
            print("OUT")
    else:
        print("OUT")