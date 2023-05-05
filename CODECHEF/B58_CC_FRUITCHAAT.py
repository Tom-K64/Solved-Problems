"""
Problem Link :
https://www.codechef.com/problems/FRUITCHAAT
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x//2)<=y:
        print(x//2)
    else:
        print(y)