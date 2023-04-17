"""
Problem Link :
https://www.codechef.com/problems/TEA
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    refill=0
    if x%y==0:
        refill=int(x/y)
    else:
        refill=int(x/y)+1
    print(refill * z)