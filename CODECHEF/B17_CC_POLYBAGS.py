"""
Problem Link :
https://www.codechef.com/problems/POLYBAGS
"""
t=int(input())
for i in range(t):
    n=int(input())
    print((n//10+1)) if n%10!=0 else print(n//10)