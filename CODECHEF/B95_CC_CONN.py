"""
Problem Link :
https://www.codechef.com/problems/CONN
"""
t=int(input())
for i in range(t):
    n=int(input())
    if n%7==0 or n%2==0:
        print("YES")
    elif n%2!=0:
        if n>7:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")