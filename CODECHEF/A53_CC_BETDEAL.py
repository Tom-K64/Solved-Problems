"""
Problem Link :
https://www.codechef.com/problems/BETDEAL
"""
t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    pa=100-a
    pb=200-(2*b)
    if pa<pb:
        print("FIRST")
    elif pb<pa:
        print("SECOND")
    else:
        print("BOTH")