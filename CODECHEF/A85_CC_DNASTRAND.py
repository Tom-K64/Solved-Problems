"""
Problem Link :
https://www.codechef.com/problems/DNASTRAND
"""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ns=""
    for i in s:
        if i=="A":
            ns+="T"
        elif i=="T":
            ns+="A"
        elif i=="C":
            ns+="G"
        elif i=="G":
            ns+="C"
    print(ns)
        
    