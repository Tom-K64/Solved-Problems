"""
Problem Link :
https://www.codechef.com/problems/INDIVISIBLE
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    k=0
    for i in range(2,100):
        if a%i!=0 and b%i!=0 and c%i!=0:
            k=i
            break
    print(k)