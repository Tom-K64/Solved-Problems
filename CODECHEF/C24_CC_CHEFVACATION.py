"""
Problem Link :
https://www.codechef.com/problems/CHEFVACATION
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if z>=(x+y):
        print("YES")
    else:
        print("NO")