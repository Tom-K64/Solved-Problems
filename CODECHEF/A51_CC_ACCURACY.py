"""
Problem Link :
https://www.codechef.com/problems/ACCURACY
"""
t=int(input())
for i in range(t):
    x=int(input())
    print(3-(x%3)) if x%3!=0 else print(0)