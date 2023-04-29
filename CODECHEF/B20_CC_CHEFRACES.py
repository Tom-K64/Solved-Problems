"""
Problem Link :
https://www.codechef.com/problems/CHEFRACES
"""
t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    l=[a,b]
    if x in l and y in l:
        print(0)
    elif x in l or y in l:
        print(1)
    else:
        print(2)