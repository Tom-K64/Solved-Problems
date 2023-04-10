"""
Problem Link :
https://www.codechef.com/problems/CHEAPFOOD
"""
t=int(input())
for i in range(t):
    x=int(input())
    print(100) if x<=1000 else print(int(x/10))