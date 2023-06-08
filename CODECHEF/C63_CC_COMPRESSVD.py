"""
Problem Link :
https://www.codechef.com/problems/COMPRESSVD
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    frames=n
    for j in range(n-1):
        if arr[j]==arr[j+1]:
            frames-=1
    print(frames)