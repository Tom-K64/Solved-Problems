"""
Problem Link :
https://www.codechef.com/problems/RANKLISTPAGE
"""
t=int(input())
for i in range(t):
    x=int(input())
    print(int(x/25)) if x%25==0 else print(int(x/25)+1)