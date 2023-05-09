"""
Problem Link :
https://www.codechef.com/problems/FLOW005
"""
t=int(input())
for i in range(t):
    n=int(input())
    count,d=0,[100,50,10,5,2,1]
    for i in d:
        count+=(n//i)
        n=n%i
        if n==0:
            break
    print(count)