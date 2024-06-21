l=[0,1,0,2,1,0,1,3,2,1,2,1]
m1=l[0];s=0;s1=0
for i in range(len(l)):
    if l[i+1:] and max(l[i+1:])<m1:
        m1=max(l[i+1:])
    if l[i]<m1:
        s1+=(m1-l[i])
    else:
        m1=l[i]
        s=s1
print(s,s1)   