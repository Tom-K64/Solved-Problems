"""
Problem Link :
https://www.codechef.com/problems/FLOORS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x%10!=0:
        fx=x//10
    else:
        fx=(x//10)-1
    if y%10!=0:
        fy=y//10
    else:
        fy=(y//10)-1
    print(abs(fx-fy))