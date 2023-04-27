"""
Problem Link :
https://www.codechef.com/problems/SELFDEF
"""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    w=0
    for i in a:
        if i >=10 and i<=60:
            w+=1
    print(w)