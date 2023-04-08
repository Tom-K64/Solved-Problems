"""
Problem Link :
https://www.codechef.com/problems/BOBBANK
"""
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    print(w+((x-y)*z))