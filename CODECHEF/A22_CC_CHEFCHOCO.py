"""
Problem Link :
https://www.codechef.com/problems/CHEFCHOCO
"""
t=int(input())
for i in range(t):
    c,x,y=map(int,input().split())
    print(y*(c-x))