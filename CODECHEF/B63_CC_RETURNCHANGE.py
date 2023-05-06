"""
Problem Link :
https://www.codechef.com/problems/RETURNCHANGE
"""
t=int(input())
for i in range(t):
    x=int(input())
    if (x%10)>=5:
        print(100-(10-((x%10))+x))
    else:
        print(100-(x-(x%10)))
    