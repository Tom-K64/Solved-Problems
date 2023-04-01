"""
Problem Link :
https://www.codechef.com/problems/CMASKS
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x*100)<(y*10):
        print("Disposable")
    else:
        print("Cloth")