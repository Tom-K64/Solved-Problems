"""
Problem Link :
https://www.codechef.com/problems/WATERCOOLER2
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<=x:
        print(0)
    else:
        if y%x==0:
            print((y//x)-1)
        else:
            print(y//x)