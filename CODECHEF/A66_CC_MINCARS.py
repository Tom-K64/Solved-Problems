"""
Problem Link :
https://www.codechef.com/problems/MINCARS
"""
t=int(input())
for i in range(t):
    n=int(input())
    print(int(n/4)) if n%4==0 else print(int(n/4)+1)