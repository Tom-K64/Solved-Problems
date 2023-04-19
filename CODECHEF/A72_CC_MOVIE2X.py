"""
Problem Link :
https://www.codechef.com/problems/MOVIE2X
"""
x,y=map(int,input().split())
print(x-int(y/2)) if y<=x*2 else print(0)
    