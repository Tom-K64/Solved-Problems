"""
Problem Link :
https://www.codechef.com/problems/SUMTRIAN
"""
t=int(input())
for _ in range(t):
    n= int(input())
    lst=[]
    for i in range(n):
        l=list(map(int,input().split()))
        lst.append(l)
    for i in range(n-1, 0, -1) :
        for j in range(i):
            lst[i-1][j] += max( lst[i][j], lst[i][j+1])
    
    print(lst[0][0])