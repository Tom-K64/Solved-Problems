"""
Problem Link :
https://www.codechef.com/problems/MAYOR_PARTY
"""
t=int(input())
for i in range(t):
    pa,pb,pc=map(int,input().split())
    if (pa+pc)<pb:
        print(pb)
    else:
        print(pa+pc)