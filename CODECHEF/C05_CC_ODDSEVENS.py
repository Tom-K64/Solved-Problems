"""
Problem Link :
https://www.codechef.com/problems/ODDSEVENS
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print("Bob")
    else:
        print("Alice")