import string as s#USING LISTS
l=list(s.ascii_lowercase)
u=list(s.ascii_uppercase)
s=input();s1=""
n=int(input())
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        c=l.index(i)
        s1+=l[c-n]
    else:
        c=u.index(i)
        s1+=u[c-n]
print(s1)