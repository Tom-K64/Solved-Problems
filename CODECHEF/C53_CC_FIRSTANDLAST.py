"""
Problem Link :
https://www.codechef.com/problems/FIRSTANDLAST
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    m=arr[0]+arr[-1]
    for j in range(n-1):
        s=arr[j]+arr[j+1]
        if s>m:
            m=s
    print(m)