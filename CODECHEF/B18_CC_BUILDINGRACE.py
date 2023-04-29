"""
Problem Link :
https://www.codechef.com/problems/BUILDINGRACE
"""
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    chef,chefina=a/x,b/y
    if chef<chefina:
        print("CHEF")
    elif chefina<chef:
        print("CHEFINA")
    else:
        print("BOTH")