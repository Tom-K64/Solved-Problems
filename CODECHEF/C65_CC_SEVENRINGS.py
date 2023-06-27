"""
Problem Link :
https://www.codechef.com/problems/SEVENRINGS
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print("YES") if (n*x)>9999 and (n*x)<100000 else print("NO")