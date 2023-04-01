"""
Problem Link :
https://www.codechef.com/problems/SPECIALITY
"""
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print("Setter") if x>y and x>z else print("Tester") if y>x and y>z else print("Editorialist")