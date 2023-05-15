"""
Problem Link :
https://www.codechef.com/problems/DEVSPORTS
"""
t=int(input())
for i in range(t):
    z,y,a,b,c=map(int,input().split())
    print("YES") if (z-y)>=(a+b+c) else print("NO")