"""
Problem Link :
https://www.codechef.com/problems/OLYRANK
"""
t=int(input())
for i in range(t):
    g1,s1,b1,g2,s2,b2=map(int,input().split())
    m1,m2=g1+s1+b1,g2+s2+b2
    if m1>m2:
        print(1)
    else:
        print(2)