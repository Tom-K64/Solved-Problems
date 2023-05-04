"""
Problem Link :
https://www.codechef.com/problems/HARDBET
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a<b and a<c:
        print("Draw")
    elif b<c and b<a:
        print("Bob")
    else:
        print("Alice")