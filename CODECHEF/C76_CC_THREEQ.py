"""
Problem Link :
https://www.codechef.com/problems/THREEQ
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    if [a,b,c].count(1)==[x,y,z].count(1):
        print("Pass")
    else:
        print("Fail")