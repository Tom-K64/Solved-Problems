"""
Problem Link :
https://www.codechef.com/problems/TVDISC
"""
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    print("FIRST") if (a-c)<(b-d) else print("SECOND") if (b-d)<(a-c) else print("ANY")