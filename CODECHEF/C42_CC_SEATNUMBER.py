"""
Problem Link :
https://www.codechef.com/problems/SEATNUMBER
"""
t=int(input())
for i in range(t):
    n=int(input())
    if n<11:
        print("Lower Double")
    elif n<16:
        print("Lower Single")
    elif n<26:
        print("Upper Double")
    else:
        print("Upper Single")