"""
Problem Link :
https://www.codechef.com/problems/FLOW011
"""
t=int(input())
for i in range(t):
    s=int(input())
    if s<1500:
        print(s+(s*0.1)+(s*0.9))
    else:
        print(s+500+(s*0.98))
        