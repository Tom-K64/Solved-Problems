"""
Problem Link :
https://www.codechef.com/problems/PASSORFAIL
"""
t=int(input())
for i in range(t):
    n,x,p=map(int,input().split())
    print("PASS") if ((x*3)-(n-x))>=p else print("FAIL")