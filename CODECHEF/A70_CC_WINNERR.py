"""
Problem Link :
https://www.codechef.com/problems/WINNERR
"""
t=int(input())
for i in range(t):
    pa,pb,qa,qb=map(int,input().split())
    ma,mb=max(pa,pb),max(qa,qb)
    print("TIE") if ma==mb else print("P") if ma<mb else print("Q")