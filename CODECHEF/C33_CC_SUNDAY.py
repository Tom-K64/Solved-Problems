"""
Problem Link :
https://www.codechef.com/problems/SUNDAY
"""
t=int(input())
for i in range(t):
    n=int(input())
    days=list(map(int,input().split()))
    count=0
    for j in days:
        if (j+1)%7==0 or j%7==0:
            count+=1
    print(8+n-count)