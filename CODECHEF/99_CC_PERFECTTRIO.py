"""
Problem Link :
https://www.codechef.com/problems/PERFECTTRIO
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a>=b and a>=c):
        print("YES") if (b+c)==a else print("NO")
    elif(b>=c and b>=a):
        print("YES") if (a+c)==b else print("NO")
    else:
        print("YES") if (a+b)==c else print("NO")
            