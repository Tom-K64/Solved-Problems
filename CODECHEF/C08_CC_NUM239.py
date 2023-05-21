"""
Problem Link :
https://www.codechef.com/problems/NUM239
"""
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    count=0
    for j in range(l,r+1):
        if str(j)[-1] in "239":
            count+=1
    print(count)