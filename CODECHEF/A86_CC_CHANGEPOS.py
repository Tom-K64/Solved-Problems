"""
Problem Link :
https://www.codechef.com/problems/CHANGEPOS
"""
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    print(2) if a==c or b==d else print(1)