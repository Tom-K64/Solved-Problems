"""
Problem Link :
https://www.codechef.com/problems/CUTOFF
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    print(a[x-1]-1)