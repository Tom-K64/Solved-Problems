"""
Problem Link :
https://www.codechef.com/problems/SUMNEQ
"""
n=int(input())
count=0
for i in range(1,n+1):
    for j in range(1,n+1-i):
        if i+j==n:
            count+=1
print(count)