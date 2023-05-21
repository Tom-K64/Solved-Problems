"""
Problem Link :
https://www.codechef.com/problems/DRUNKALK
"""
t=int(input())
for i in range(t):
    k= int(input())
    if k%2==0:
        print(k)
    else:
        print(k+2)