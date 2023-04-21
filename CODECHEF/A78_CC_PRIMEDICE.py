"""
Problem Link :
https://www.codechef.com/problems/PRIMEDICE
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    sum,count=a+b,0
    for i in range(2,sum):
        if sum%i==0:
            count+=1
            break
    if count==1:
        print("BOB")
    else:
        print("ALICE")
    