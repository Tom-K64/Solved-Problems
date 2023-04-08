"""
Problem Link :
https://www.codechef.com/problems/MANGOES
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(int((z-y)/x))