"""
Problem Link :
https://www.codechef.com/problems/NEGPROD
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a<0 or b<0 or c<0) and (a>0 or b>0 or c>0):
        print("YES")
    else:
        print("NO")