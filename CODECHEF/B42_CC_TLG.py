"""
Problem Link :
https://www.codechef.com/problems/TLG
"""
n=int(input())
w,l=0,0
lead1,lead2=0,0
sc1,sc2=0,0
for i in range(n):
    x,y=map(int,input().split())
    sc1+=x
    sc2+=y
    if sc1>sc2:
        lead1=max(lead1,sc1-sc2)
    else:
        lead2=max(lead2,sc2-sc1)
if lead1>lead2:
    print(1,lead1)
else:
    print(2,lead2)
    
    