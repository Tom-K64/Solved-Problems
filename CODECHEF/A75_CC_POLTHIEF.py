"""
Problem Link :
https://www.codechef.com/problems/POLTHIEF
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(abs(x-y))