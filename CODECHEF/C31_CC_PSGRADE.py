"""
Problem Link :
https://www.codechef.com/problems/PSGRADE
"""
t=int(input())
for i in range(t):
    am,bm,cm,tm,a,b,c=map(int,input().split())
    if a>=am and b>=bm and c>=cm and (a+b+c)>=tm :
        print("YES")
    else:
        print("NO")