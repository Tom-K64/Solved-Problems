"""
Problem Link :
https://www.codechef.com/problems/MAXTASTE
"""
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    print(max(a,b)+max(c,d))