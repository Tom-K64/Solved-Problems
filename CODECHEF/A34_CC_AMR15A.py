"""
Problem Link :
https://www.codechef.com/problems/AMR15A
"""
t=int(input())
a=list(map(int,input().split()))
ceven,codd=0,0
for i in a:
    if i%2==0:
        ceven+=1
    else:
        codd+=1
print("READY FOR BATTLE") if ceven>codd else print("NOT READY")