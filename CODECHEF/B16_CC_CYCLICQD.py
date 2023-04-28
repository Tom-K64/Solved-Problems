"""
Problem Link :
https://www.codechef.com/problems/CYCLICQD
"""
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    print("YES") if (a+c)==180 else print("NO")