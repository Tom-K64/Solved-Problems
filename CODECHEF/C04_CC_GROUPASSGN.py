"""
Problem Link :
https://www.codechef.com/problems/GROUPASSGN
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print((2*n)+1-x)