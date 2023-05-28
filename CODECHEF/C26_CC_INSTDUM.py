"""
Problem Link :
https://www.codechef.com/problems/INSTDUM
"""
t=int(input())
for i in range(t):
    n=int(input())
    runs=list(map(int,input().split()))
    ball,run,count=0,0,0
    for r in runs:
        ball+=1
        run+=r
        if (run/ball)*100==100:
            count+=1
    print(count)