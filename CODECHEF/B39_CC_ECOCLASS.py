"""
Problem Link :
https://www.codechef.com/problems/ECOCLASS
"""
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    d=list(map(int,input().split()))
    count=0
    for i in range(n):
        if s[i]==d[i]:
            count+=1
    print(count)