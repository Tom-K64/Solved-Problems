"""
Problem Link:
https://www.codechef.com/problems/FINE
"""
t=int(input())
for i in range(t):
    x=int(input())
    if x<=70:
        print(0)
    elif x>70 and x<=100:
        print(500)
    else:
        print(2000)
       
