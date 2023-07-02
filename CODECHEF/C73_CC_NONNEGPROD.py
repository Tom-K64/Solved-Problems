"""
Problem Link :
https://www.codechef.com/problems/NONNEGPROD
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr.count(0)==0:
        count=0
        for ele in arr:
            if ele<0:
                count+=1
        if count%2==0:
            print(0)
        else:
            print(1)
    else:
        print(0)
        