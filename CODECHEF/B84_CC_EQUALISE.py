"""
Problem Link :
https://www.codechef.com/problems/EQUALISE
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print("YES")
    else:
        mn,mx=min(a,b),max(a,b)
        while(mn<mx):
            mn*=2
        if mn == mx:
            print("YES")
        else:
            print("NO")