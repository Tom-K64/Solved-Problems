"""
Problem Link :
https://www.codechef.com/problems/BUDGET_
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print("YES") if x>=(y*30) else print("NO")