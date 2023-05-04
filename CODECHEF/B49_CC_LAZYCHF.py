"""
Problem Link :
https://www.codechef.com/problems/LAZYCHF
"""
t=int(input())
for i in range(t):
    x,m,d=map(int,input().split())
    print(x*m)if (x*m)<=(x+d) else print(x+d)