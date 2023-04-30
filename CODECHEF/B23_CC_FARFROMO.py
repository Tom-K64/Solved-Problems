"""
Problem Link :
https://www.codechef.com/problems/FARFROMO
"""
import math
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    # x1,y1,x2,y2=abs(x1),abs(y1),abs(x2),abs(y2)
    Alex=math.sqrt((x1*x1)+(y1*y1))
    Bob=math.sqrt((x2*x2)+(y2*y2))
    if Alex>Bob:
        print("ALEX")
    elif Alex<Bob:
        print("BOB")
    else:
        print("EQUAL")