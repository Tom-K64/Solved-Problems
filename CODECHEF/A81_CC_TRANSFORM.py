"""
Problem Link :
https://www.codechef.com/problems/TRANSFORM
"""
t=int(input())
for i in range(t):
    x=int(input())
    m=x%3
    print("HUGE") if m==1 else print("SMALL") if m==2 else print("NORMAL")