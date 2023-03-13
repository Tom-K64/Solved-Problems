"""
Problem Link :
https://www.codechef.com/problems/JERRYCHASE
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y>x:
        print("YES")
    else:
        print("NO")