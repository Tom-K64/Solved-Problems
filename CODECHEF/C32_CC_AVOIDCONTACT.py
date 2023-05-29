"""
Problem Link :
https://www.codechef.com/problems/AVOIDCONTACT
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x==y:
        print((2*y)-1)
    else:
        print(x+y)