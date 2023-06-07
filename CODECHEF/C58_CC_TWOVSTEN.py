"""
Problem Link :
https://www.codechef.com/problems/TWOVSTEN
"""
t=int(input())
for i in range(t):
    x=int(input())
    count=0
    if x%5==0:
        if x%10==0:
            print(count)
        else:
            while x%10!=0:
                x=x*2
                count+=1
            print(count)
    else:
        print(-1)