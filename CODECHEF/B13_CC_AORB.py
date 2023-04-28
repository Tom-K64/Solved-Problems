"""
Problem Link :
https://www.codechef.com/problems/AORB
"""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    
    xy=(500-(x*2))+(1000-((x+y)*4))
    yx=(1000-(y*4))+(500-((x+y)*2))
    print(max(xy,yx))