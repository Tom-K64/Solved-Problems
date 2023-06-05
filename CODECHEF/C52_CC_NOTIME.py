"""
Problem Link :
https://www.codechef.com/problems/NOTIME
"""
n,h,x=map(int,input().split())
arr=list(map(int,input().split()))
if (h-x) in arr:
    print("YES")
else:
    print("NO")
