"""
Problem Link :
https://www.codechef.com/problems/KITCHENSPICE
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x<4:
        print("MILD")
    elif x>=4 and x<7:
        print("MEDIUM")
    else:
        print("HOT")
    