"""
Problem Link :
https://www.codechef.com/problems/SST
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    VA,VB=a*10,b*5
    print("ANY") if VA==VB else print("FIRST") if VA>VB else print("SECOND")