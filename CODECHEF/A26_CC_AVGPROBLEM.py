"""
Problem Link :
https://www.codechef.com/problems/AVGPROBLEM
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print("YES") if ((a+b)/2)>c else print("NO")