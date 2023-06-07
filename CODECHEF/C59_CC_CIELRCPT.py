"""
Problem Link :
https://www.codechef.com/problems/CIELRCPT
"""
t=int(input())
menu=[2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for i in range(t):
    n=int(input())
    j,count=0,0
    while n!=0:
        if n<menu[j]:
            j+=1
            continue
        else:
            n-=menu[j]
            j=0
            count+=1
    print(count)