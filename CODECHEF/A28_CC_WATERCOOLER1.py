"""
Problem Link :
https://www.codechef.com/problems/WATERCOOLER1
"""
t=int(input())
for i in range(t):
    x,y,m=map(int,input().split())
    print("YES") if y>(x*m) else print("NO")