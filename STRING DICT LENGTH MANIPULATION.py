s="hello:5438,car:214,book:8799,apple:2187"
s1=''
l=dict(i.split(":")for i in s.split(","))
print(l)
for i in l:
    n=len(i)
    print(n,l[i])
    if str(n) in l[i]:
        s1+=i[n-1]
    else:
        f=1
        for j in range(n-1,0,-1):
            if str(j) in l[i]:
                s1+=i[j-1]
                f=0
                break
        if f:
            s1+='x'
print(s1)