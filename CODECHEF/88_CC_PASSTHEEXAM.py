"""
Problem Link :
https://www.codechef.com/problems/PASSTHEEXAM
"""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+b+c)>=100:
        if a>=10 and b>=10 and c>=10:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")