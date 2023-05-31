"""
Problem Link :
https://www.codechef.com/problems/PENALTY
"""
t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    ta,tb=0,0
    for j in range(10):
        if j%2==0:
            ta+=x[j]
        else:
            tb+=x[j]
    if ta==tb:
        print(0)
    elif ta>tb:
        print(1)
    else:
        print(2)