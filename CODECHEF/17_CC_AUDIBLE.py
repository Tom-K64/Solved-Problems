"""
Problem Link :
https://www.codechef.com/problems/AUDIBLE
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x>66 and x<45001:
        print("YES")
    else:
        print("NO")