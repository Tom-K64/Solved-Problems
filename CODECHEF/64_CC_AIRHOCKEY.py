"""
Problem Link :
https://www.codechef.com/problems/AIRHOCKEY
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print(7-x)
    else:
        print(7-y)