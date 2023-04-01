"""
Problem Link :
https://www.codechef.com/problems/CANDYSTORE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<=x:
        print(y)
    else:
        print(x+((y-x)*2))