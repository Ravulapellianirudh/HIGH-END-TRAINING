s='tu5g2k1h8'
s1='g5g8d6h3'
l=[];m=11
for i in s+s1:
    if i.isdigit() and int(i)%2==0 and m>int(i):
        m=int(i)
    if i.isdigit() and int(i) not in l:
        l.append(int(i))
l.remove(m)
l=sorted(l,reverse=True)
s=0
for i in l:
    s=s*10+i
s=s*10+m
print(l,m,s)
        