"""
Problem Link :
https://www.codechef.com/problems/WORDLE
"""
t=int(input())
for i in range(t):
    h=input()
    g=input()
    m=""
    for i in range(5):
        if h[i]==g[i]:
            m+="G"
        else:
            m+="B"
    print(m)