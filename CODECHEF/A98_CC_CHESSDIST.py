"""
Problem Link :
https://www.codechef.com/problems/CHESSDIST
"""
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    print(max(abs(x1-x2),abs(y1-y2)))