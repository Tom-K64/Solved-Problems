"""
Problem Link :
https://www.codechef.com/problems/LOOP
"""
t=int(input())
for i in range(t):
    a,b,m=map(int,input().split())
    print(min((m-abs(a-b)),abs(a-b)))