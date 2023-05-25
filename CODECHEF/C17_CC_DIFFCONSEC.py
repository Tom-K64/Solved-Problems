"""
Problem Link :
https://www.codechef.com/problems/DIFFCONSEC
"""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    c=0
    for j in range(n-1):
        if s[j]==s[j+1]:
            c+=1
    print(c)