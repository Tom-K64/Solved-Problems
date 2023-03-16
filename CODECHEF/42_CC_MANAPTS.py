"""
Problem Link:
https://www.codechef.com/problems/MANAPTS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(int(y/x))