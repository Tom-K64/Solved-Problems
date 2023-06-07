"""
Problem Link :
https://www.codechef.com/problems/WATERFILLING
"""
t=int(input())
for i in range(t):
    b1,b2,b3=map(int,input().split())
    if [b1,b2,b3].count(0)>=2:
        print("Water filling time")
    else:
        print("Not now")