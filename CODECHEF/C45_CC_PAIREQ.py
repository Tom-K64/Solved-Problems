"""
Problem Link :
https://www.codechef.com/problems/PAIREQ
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[arr.count(a) for a in arr]
    print(n-max(l))
    