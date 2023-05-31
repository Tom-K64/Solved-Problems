"""
Problem Link :
https://www.codechef.com/problems/SOLBLTY
"""
t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    print((a+((100-x)*b))*10)