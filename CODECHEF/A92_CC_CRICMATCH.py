"""
Problem Link :
https://www.codechef.com/problems/CRICMATCH
"""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print("YES") if n<=(m*6*6) else print("NO")