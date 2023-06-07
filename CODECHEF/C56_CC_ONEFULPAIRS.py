"""
Problem Link :
https://www.codechef.com/problems/ONEFULPAIRS
"""
a,b=map(int,input().split())
if a+b+(a*b)==111:
    print("YES")
else:
    print("NO")