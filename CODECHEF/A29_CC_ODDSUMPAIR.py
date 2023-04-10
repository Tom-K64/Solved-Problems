"""
Problem Link :
https://www.codechef.com/problems/ODDSUMPAIR
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print("YES") if (a+b)%2==1 or (b+c)%2==1 or (a+c)%2==1 else print("NO")
    # if (a%2==0 or b%2==0 or c%2==0) and (a%2==1 or b%2==1 or c%2==1):
    #     print("YES")
    # else:
    #     print("NO")