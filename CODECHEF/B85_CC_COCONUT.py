"""
Problem Link :
https://www.codechef.com/problems/COCONUT
"""
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    if x%a==0:
        ca=x//a
    else:
        ca=(x//a)+1
    if y%b==0:
        cb=y//b
    else:
        cb=(y//b)+1
    print(ca+cb)