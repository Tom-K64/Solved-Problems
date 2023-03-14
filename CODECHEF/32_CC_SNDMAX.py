"""
Problem Link :
https://www.codechef.com/problems/SNDMAX
"""
t=int(input())
for i in range(t):
    lst=list(map(int,input().split()))
    lst.remove(max(lst))
    print(max(lst))