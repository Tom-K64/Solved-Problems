"""
Problem Link :
https://www.codechef.com/problems/SOCKS1
"""
a,b,c=map(int,input().split())
if a==b or a==c or b==c:
    print("YES")
else:
    print("NO")