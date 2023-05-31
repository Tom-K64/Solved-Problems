"""
Problem Link :
https://www.codechef.com/problems/TWORANGES
"""
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    l=[j for j in range(a,b+1)]
    for j in range(c,d+1):
        if j not in l:
            l.append(j)
    print(len(l))