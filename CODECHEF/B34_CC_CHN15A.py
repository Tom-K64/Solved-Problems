"""
Problem Link :
https://www.codechef.com/problems/CHN15A
"""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    chars=list(map(int,input().split()))
    chars=list(map(lambda x:x+k,chars))
    wolve=0
    for num in chars:
        if num%7==0:
            wolve+=1
    print(wolve)