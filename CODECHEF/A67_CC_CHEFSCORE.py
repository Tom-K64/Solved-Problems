"""
Problem Link :
https://www.codechef.com/problems/CHEFSCORE
"""
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    print("YES") if y<=(n*x) and y%x==0 else print("NO")