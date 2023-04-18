"""
Problem Link :
https://www.codechef.com/problems/QUALIFY
"""
t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    print("QUALIFY") if a+(2*b) >= x else print("NOTQUALIFY")