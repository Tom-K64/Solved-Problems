"""
Problem Link :
https://www.codechef.com/problems/BOOKPACK
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if y%z==0:
        fes=y//z
    else:
        fes=(y//z)+1
    print(x*fes)