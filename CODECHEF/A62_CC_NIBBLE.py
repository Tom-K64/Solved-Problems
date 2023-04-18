"""
Problem Link :
https://www.codechef.com/problems/NIBBLE
"""
t=int(input())
for i in range(t):
    n=int(input())
    print("GOOD") if n%4==0 else print("NOT GOOD")