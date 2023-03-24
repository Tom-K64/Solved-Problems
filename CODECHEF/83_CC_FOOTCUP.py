"""
Problem Link :
https://www.codechef.com/problems/FOOTCUP
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if x==y and (x>0 and y>0) else print("NO")