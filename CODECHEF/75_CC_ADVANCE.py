"""
Problem Link :
https://www.codechef.com/problems/ADVANCE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>=x and y<=(x+200):
        print("YES")
    else:
        print("NO")