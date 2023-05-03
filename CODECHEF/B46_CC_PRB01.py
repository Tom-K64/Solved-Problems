"""
Problem Link :
https://www.codechef.com/problems/PRB01
"""
t=int(input())
for i in range(t):
    n=int(input())
    count=0
    for num in range(2,n):
        if n%num==0:
            count+=1
            break
    if count==0 and n>1:
        print("yes")
    else:
        print("no")