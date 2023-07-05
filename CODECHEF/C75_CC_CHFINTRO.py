"""
Problem Link :
https://www.codechef.com/problems/CHFINTRO
"""
n,r=map(int,input().split())
arr=[]
for i in range(n):
    temp=int(input())
    if temp>=r:
        print("Good boi")
    else:
        print("Bad boi")