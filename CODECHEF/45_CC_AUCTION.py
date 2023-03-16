"""
Problem Link:
https://www.codechef.com/problems/AUCTION
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a>=b and a>=c:
        print("ALICE")
    elif b>=a and b>=c:
        print("BOB")
    else:
        print("CHARLIE")