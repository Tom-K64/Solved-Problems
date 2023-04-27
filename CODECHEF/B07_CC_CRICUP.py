"""
Problem Link :
https://www.codechef.com/problems/CRICUP
"""
t=int(input())
for i in range(t):
    x,y,d=map(int,input().split())
    print("YES") if abs(x-y)<=d else print("NO")