"""
Problem Link :
https://www.codechef.com/problems/BLACKJACK
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(21-a-b) if (21-a-b)<=10 else print(-1)