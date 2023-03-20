"""
Problem Link:
https://www.codechef.com/problems/COMPLEXITY
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("YES")
    else:
        print("NO")