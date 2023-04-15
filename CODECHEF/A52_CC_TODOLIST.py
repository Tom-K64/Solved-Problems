"""
Problem Link :
https://www.codechef.com/problems/TODOLIST
"""
t=int(input())
for i in range(t):
    n=int(input())
    d=list(map(int,input().split()))
    count=0
    for i in d:
        if i>=1000:
            count+=1
    print(count)