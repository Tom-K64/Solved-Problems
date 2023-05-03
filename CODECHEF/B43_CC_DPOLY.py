"""
Problem Link :
https://www.codechef.com/problems/DPOLY
"""
t=int(input())
for i in range(t):
    n=int(input())
    pol=list(map(int,input().split()))
    degree=n-1
    for num in pol[::-1]:
        if num==0:
            degree-=1
        else:
            break
    print(degree)