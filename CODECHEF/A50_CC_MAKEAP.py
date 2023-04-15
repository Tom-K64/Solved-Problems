"""
Problem Link :
https://www.codechef.com/problems/MAKEAP
"""
t=int(input())
for i in range(t):
    a,c=map(int,input().split())
    diff=c-a
    print(a+int(diff/2)) if diff%2==0 else print(-1)
    