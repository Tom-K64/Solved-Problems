"""
Problem Link :
https://www.codechef.com/problems/TABLETS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>=(x*3):
        print("YES")
    else:
        print("NO")