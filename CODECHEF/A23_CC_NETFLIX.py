"""
Problem Link :
https://www.codechef.com/problems/NETFLIX
"""
t=int(input())
for i in range(t):
    a,b,c,x=map(int,input().split())
    print("YES") if (a+b)>=x or (b+c)>=x or (a+c)>=x else print("NO")
    