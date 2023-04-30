"""
Problem Link :
https://www.codechef.com/problems/PRESENTS
"""
t=int(input())
for i in range(t):
    n=int(input())
    div,mod=n//5,n%5
    print((div*4)+mod)
    