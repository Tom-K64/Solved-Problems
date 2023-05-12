"""
Problem Link :
https://www.codechef.com/problems/INCREAR
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x==y:
        print(0)
    elif x<y:
        print(y-x)
    else:
        z=x-y
        if z%2==0:
            print(z//2)
        else:
            print((z//2)+2)