"""
Problem Link :
https://www.codechef.com/problems/DNASTORAGE
"""
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    encode=""
    for i in range(1,(n//2)+1):
        j=s[(i-1)*2:i*2]
        if j=="00":
            encode+="A"
        elif j=="01":
            encode+="T"
        elif j=="10":
            encode+="C"
        elif j=="11":
            encode+="G"
    print(encode)
            