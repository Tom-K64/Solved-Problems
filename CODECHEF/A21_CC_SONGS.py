"""
Problem Link :
https://www.codechef.com/problems/SONGS
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(int(n/(x*3)))