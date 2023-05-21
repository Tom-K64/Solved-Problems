"""
Problem Link :
https://www.codechef.com/problems/FCTRL
"""
t=int(input())
for i in range(t):
    n,c=int(input()),0
    while n>0:
        c=c+(n//5)
        n=n//5
    print(c)