"""
Problem Link :
https://www.codechef.com/problems/FACEDIR
"""
t=int(input())
for i in range(t):
    x=int(input())
    x=x%4
    if x==0:
        print("North")
    elif x==1:
        print("East")
    elif x==2:
        print("South")
    else:
        print("West")