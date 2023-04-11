"""
Problem Link :
https://www.codechef.com/problems/CREDCOINS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(int((y*x)/100))