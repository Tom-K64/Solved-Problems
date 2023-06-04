"""
Problem Link :
https://www.codechef.com/problems/PRICECON
"""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    rev=0
    for a in arr:
        if a>k:
            rev+=(a-k)
    print(rev)