"""
Problem Link :
https://www.codechef.com/problems/GENE01
"""
c1,c2=map(str,input().split())
if c1==c2:
    print(c1)
elif c1=="R" or c2=="R":
    print("R")
elif c1=="B" or c2=="B":
    print("B")
else:
    print("G")
    