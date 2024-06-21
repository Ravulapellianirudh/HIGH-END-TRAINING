l=[4,8,2,4,4,4,8];a=[0]*max(l)
n=len(l);j=-1
for i in range(n//2 +1):
    a[l[i]-1]+=1
    if i!=n//2:
        a[l[j]-1]+=1
    j-=1
if max(a)>=n//2:
    print(a.index(max(a))+1)
    
    