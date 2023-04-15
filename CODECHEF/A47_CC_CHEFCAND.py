"""
Problem Link :
https://www.codechef.com/problems/CHEFCAND
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    need=n-x
    if(need>0):
        print(int(need/4)) if need%4==0 else print(int(need/4)+1)
    else:
        print(0)