"""
Problem Link :
https://www.codechef.com/problems/FIFTYPE
"""
t=int(input())
for i in range(t):
    n=int(input())
    if n==50:
        print(0)
    else:
        count=0
        while n!=50:
            if n>50:
                n-=3
            else:
                n+=2
            count+=1
        print(count)
            
        