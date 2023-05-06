"""
Problem Link :
https://www.codechef.com/problems/GOODWEAT
"""
t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    if x.count(0)<x.count(1):
        print("YES")
    else:
        print("NO")