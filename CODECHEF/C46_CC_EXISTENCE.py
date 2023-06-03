"""
Problem Link :
https://www.codechef.com/problems/EXISTENCE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x**4)+(4*y*y) == (4*x*x*y):
        print("YES")
    else:
        print("NO")