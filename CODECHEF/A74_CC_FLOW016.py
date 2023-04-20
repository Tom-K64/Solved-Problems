"""
Problem Link :
https://www.codechef.com/problems/FLOW016
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    def compute_gcd(gcd, y):
       while(y):
           gcd, y = y, gcd % y
       return gcd
    def compute_lcm(x, y):
       lcm = (x*y)//compute_gcd(x,y)
       return lcm
    print(compute_gcd(a,b),compute_lcm(a,b))