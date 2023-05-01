"""
Problem Link :
https://www.codechef.com/problems/BIN_BAT
"""
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    i,num=0,0
    while num!=n:
        num=2**i
        i+=1
    print((a*(i-1))+(b*(i-2)))
    