"""
Problem Link :
https://www.codechef.com/problems/NEARESTEXIT
"""
t=int(input())
for i in range(t):
    x=int(input())
    print("LEFT") if x<=50 else print("RIGHT")