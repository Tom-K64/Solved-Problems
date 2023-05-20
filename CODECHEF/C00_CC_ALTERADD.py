"""
Problem Link :
https://www.codechef.com/problems/ALTERADD
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=b-a
    if c%3==0 or (c-1)%3==0:
        print("YES")
    else:
        print("NO")