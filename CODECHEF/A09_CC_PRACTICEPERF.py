"""
Problem Link :
https://www.codechef.com/problems/PRACTICEPERF
"""
week=list(map(int,input().split()))
count=0
for i in week:
    if i>=10:
        count+=1
print(count)