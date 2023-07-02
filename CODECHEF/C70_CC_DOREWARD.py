"""
Problem Link :
https://www.codechef.com/problems/DOREWARD
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x<4:
        print("BRONZE")
    elif x>3 and x<7:
        print("SILVER")
    else:
        print("GOLD")