"""
Problem Link :
https://www.codechef.com/problems/ACTEMP
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print("YES") if a<=b and c<=b else print("NO")
    