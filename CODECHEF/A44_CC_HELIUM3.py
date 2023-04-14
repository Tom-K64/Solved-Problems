"""
Problem Link :
https://www.codechef.com/problems/HELIUM3
"""
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    print("YES") if x*y >= a*b else print("NO")