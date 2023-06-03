"""
Problem Link :
https://www.codechef.com/problems/LARGESECOND
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=max(arr)
    for j in range(arr.count(a)):
        arr.remove(a)
    print(a+max(arr))