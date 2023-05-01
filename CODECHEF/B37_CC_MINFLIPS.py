"""
Problem Link :
https://www.codechef.com/problems/MINFLIPS
"""
t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    if n%2==1:
        print(-1)
    else:
        ones,n_ones=x.count(1),x.count(-1)
        if ones==n_ones:
            print(0)
        else:
            print(abs((n//2)-ones))