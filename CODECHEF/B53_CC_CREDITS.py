"""
Problem Link :
https://www.codechef.com/problems/CREDITS
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x<35:
        print("UNDERLOAD")
    elif x>65:
        print("OVERLOAD")
    else:
        print("NORMAL")