"""
Problem Link :
https://www.codechef.com/problems/MINCOINS
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x%5==0:
        print((x//10)+1) if x%10!=0 else print(x//10)
    else:
        print(-1)