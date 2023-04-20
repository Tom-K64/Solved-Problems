"""
Problem Link :
https://www.codechef.com/problems/BATH
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(int(x/(y*2)))