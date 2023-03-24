"""
Problem Link :
https://www.codechef.com/problems/HOTCOLD
"""
t=int(input())
for i in range(t):
    c=int(input())
    print("HOT") if c>20 else print("COLD")
    