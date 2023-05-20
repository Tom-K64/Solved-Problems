"""
Problem Link :
https://www.codechef.com/problems/WHICHDIV
"""
t=int(input())
for i in range(t):
    r=int(input())
    if r<1600:
        print(3)
    elif r>=1600 and r<2000:
        print(2)
    else:
        print(1)