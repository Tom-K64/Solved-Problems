"""
Problem Link :
https://www.codechef.com/problems/JCOINS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print((x*10)+(y*5))