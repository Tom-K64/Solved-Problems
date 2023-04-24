"""
Problem Link :
https://www.codechef.com/problems/HIGHSCORE
"""
t=int(input())
for i in range(t):
    n=int(input())
    a,b,c,d=map(int,input().split())
    print(max(a,b,c,d))