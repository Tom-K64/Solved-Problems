"""
Problem Link :
https://www.codechef.com/problems/DISCUS
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print(max(a,b,c))