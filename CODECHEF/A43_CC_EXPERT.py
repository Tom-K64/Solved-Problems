"""
Problem Link :
https://www.codechef.com/problems/EXPERT
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if (y*2)>=x else print("NO")