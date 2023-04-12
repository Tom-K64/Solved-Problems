"""
Problem Link :
https://www.codechef.com/problems/RACE400M
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x<y and x<z:
        print("ALICE")
    elif y<x and y<z:
        print("BOB")
    else:
        print("CHARLIE")
    