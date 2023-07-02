"""
Problem Link :
https://www.codechef.com/problems/TEKKEN
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    m=max(a,b,c)
    if a==m:
        if [a,b,c].count(m)>1:
            if min(a,b,c)!=0:
                print("YES")
            else:
                print("NO")
        else:
            print("YES")
    else:
        print("NO")