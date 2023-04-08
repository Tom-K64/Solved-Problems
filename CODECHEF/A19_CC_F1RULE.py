"""
Problem Link :
https://www.codechef.com/problems/F1RULE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if y<=(x*1.07) else print("NO")