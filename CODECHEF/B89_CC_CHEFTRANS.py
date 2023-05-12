"""
Problem Link :
https://www.codechef.com/problems/CHEFTRANS
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    pb=x+y
    if pb==z:
        print("EQUAL")
    elif pb<z:
        print("PLANEBUS")
    else:
        print("TRAIN")