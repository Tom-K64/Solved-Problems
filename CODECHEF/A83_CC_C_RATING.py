"""
Problem Link :
https://www.codechef.com/problems/C_RATING
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<y:
        need=y-x
        print(need//8) if need%8==0 else print((need//8)+1)
    else:
        print(0)