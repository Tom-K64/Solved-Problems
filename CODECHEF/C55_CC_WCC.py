"""
Problem Link :
https://www.codechef.com/problems/WCC
"""
t=int(input())
for i in range(t):
    x=int(input())
    s=input()
    c,n=s.count('C'),s.count('N')
    if c>n:
        print(60*x)
    elif n>c:
        print(40*x)
    else:
        print(55*x)