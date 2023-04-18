"""
Problem Link :
https://www.codechef.com/problems/ELECTN
"""
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    age=list(map(int,input().split()))
    eligible=0
    for i in age:
        if i>=x:
            eligible+=1
    print(eligible)