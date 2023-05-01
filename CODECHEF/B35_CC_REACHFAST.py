"""
Problem Link :
https://www.codechef.com/problems/REACHFAST
"""
t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    if x==y:
        print(0)
    else:
        z=abs(x-y)
        if z<k:
            print(1)
            
        else:
            if z%k==0:
                print(z//k)
            else:
                print((z//k)+1)