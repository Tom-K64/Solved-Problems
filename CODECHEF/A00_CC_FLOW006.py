"""
Problem Link :
https://www.codechef.com/problems/FLOW006
"""
T=int(input())
for i in range(T):
    num=int(input())
    sum=0
    for j in str(num):
        sum+=int(j)
    print(sum)
