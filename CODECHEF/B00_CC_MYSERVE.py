"""
Problem Link :
https://www.codechef.com/problems/MYSERVE
"""
t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    serve=p+q+1
    if serve%2==1:
        serve+=1
    print("BOB") if (serve/2)%2==0 else print("ALICE")
            