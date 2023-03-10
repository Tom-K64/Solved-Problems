"""
Problem Link :
https://www.codechef.com/problems/TAXES
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x>100:
        print(x-10)
    else:
        print(x)