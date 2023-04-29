"""
Problem Link :
https://www.codechef.com/problems/ACS
"""
t=int(input())
for i in range(t):
    p=int(input())
    np=(p//100)+(p%100)
    print(np) if np<=10 else print(-1)