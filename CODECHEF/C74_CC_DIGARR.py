"""
Problem Link :
https://www.codechef.com/problems/DIGARR
"""
t=int(input())
for i in range(t):
    d=int(input())
    n=input()
    if ("0" in n) or ("5" in n):
        print("YES")
    else:
        print("NO")
    