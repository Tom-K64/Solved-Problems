"""
Problem Link :
https://www.codechef.com/problems/CANDYDIST
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if x%y==0 and (x//y)%2==0 else print("NO")