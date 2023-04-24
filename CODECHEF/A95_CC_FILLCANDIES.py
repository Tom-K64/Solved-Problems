"""
Problem Link :
https://www.codechef.com/problems/FILLCANDIES
"""
t=int(input())
for i in range(t):
    n,k,m=map(int,input().split())
    print(n//(k*m)) if n%(k*m)==0 else print(n//(k*m)+1)