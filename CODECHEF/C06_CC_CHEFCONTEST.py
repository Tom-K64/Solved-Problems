"""
Problem Link :
https://www.codechef.com/problems/CHEFCONTEST
"""
t=int(input())
for i in range(t):
    x,y,p,q=map(int,input().split())
    a,b=(x+(p*10)),(y+(q*10))
    if a<b:
        print("CHEF")
    elif a>b:
        print("CHEFINA")
    else:
        print("DRAW")