"""
Problem Link :
https://www.codechef.com/problems/TCKTFINE
"""
t=int(input())
for i in range(t):
    x,p,q=map(int,input().split())
    print((p-q)*x)