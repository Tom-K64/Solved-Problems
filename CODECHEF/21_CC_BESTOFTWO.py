"""
Problem Link :
https://www.codechef.com/problems/BESTOFTWO
"""
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    print(max(X,Y))