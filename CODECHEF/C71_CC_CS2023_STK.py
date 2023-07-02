"""
Problem Link :
https://www.codechef.com/problems/CS2023_STK
"""
def count_streak(lst):
    count=0
    streak=[]
    for i in lst:
        if i==0:
            streak.append(count)
            count=0
        else:
            count+=1
    streak.append(count)
    return max(streak)
t=int(input())
for i in range(t):
    n=int(input())
    om=list(map(int,input().split()))
    addy=list(map(int,input().split()))
    streak_om,streak_addy=count_streak(om),count_streak(addy)
    if streak_om == streak_addy:
        print("DRAW")
    elif streak_om>streak_addy:
        print("Om")
    else:
        print("Addy")