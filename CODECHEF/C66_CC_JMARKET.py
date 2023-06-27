"""
Problem Link :
https://www.codechef.com/problems/JMARKET
"""
t=int(input())
for i in range(t):
    x,a,b,c=map(int,input().split())
    price=[a,b,c]
    price.sort()
    print((price[0]*(x-1))+price[1])