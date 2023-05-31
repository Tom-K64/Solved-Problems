"""
Problem Link :
https://www.codechef.com/problems/SAVWATER
"""
t=int(input())
for i in range(t):
    h,x,y,c=map(int,input().split())
    if c>=(x+(y//2))*h:
        print("YES")
    else:
        print("NO")