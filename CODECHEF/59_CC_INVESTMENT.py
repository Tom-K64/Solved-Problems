"""
Problem Link:
https://www.codechef.com/problems/INVESTMENT
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=(y*2):
        print("YES")
    else:
        print("NO")