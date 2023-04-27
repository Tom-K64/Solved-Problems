"""
Problem Link :
https://www.codechef.com/problems/SPEEDTEST
"""
t=int(input())
for i in range(t):
    a,x,b,y=map(int,input().split())
    sa,sb=a/x,b/y
    if sa>sb:
        print("ALICE")
    elif sb>sa:
        print("BOB")
    else:
        print("EQUAL")