"""
Problem Link :
https://www.codechef.com/problems/WTRMIXING
"""
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    required=a-b
    if required<0:
        print("YES") if x>=abs(required) else print("NO")
    elif required>0:
        print("YES") if y>=abs(required) else print("NO")
    else:
        print("YES")