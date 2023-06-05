"""
Problem Link :
https://www.codechef.com/problems/CHFCLASS
"""
t=int(input())
for i in range(t):
    n=int(input())
    if (n+1)%7==0:
        print((n//7)+1)
    else:
        print(n//7)