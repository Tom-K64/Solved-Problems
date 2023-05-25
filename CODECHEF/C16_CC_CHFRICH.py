"""
Problem Link :
https://www.codechef.com/problems/CHFRICH
"""
t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    if (b-a)%x==0:
        print((b-a)//x)
    else:
        print(((b-a)//x)+1)