"""
Problem Link :
https://www.codechef.com/problems/SALE
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print(a+b+c-min(a,b,c))