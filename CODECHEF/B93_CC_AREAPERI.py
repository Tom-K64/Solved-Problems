"""
Problem Link :
https://www.codechef.com/problems/AREAPERI
"""
l=int(input())
b=int(input())
a,p=l*b,2*(l+b)
if a>p:
    print("Area")
    print(a)
elif p>a:
    print("Peri")
    print(p)
else:
    print("Eq")
    print(a)