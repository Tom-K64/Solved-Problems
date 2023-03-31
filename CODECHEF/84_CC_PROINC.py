"""
Problem Link :
https://www.codechef.com/problems/PROINC
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(y+int(x/10))