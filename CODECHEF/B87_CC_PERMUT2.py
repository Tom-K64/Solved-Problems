"""
Problem Link :
https://www.codechef.com/problems/PERMUT2
"""
n=int(input())
while(n!=0):
    p=list(map(int,input().split()))
    q=p.copy()
    for i in range(n):
        q[p[i]-1]=i+1 
    if p!=q:
        print("not ambiguous")
    else:
        print("ambiguous")
    n=int(input())