l=[4,9,8,2,14,3,5,6]
j=1
k=2
for i in range(len(l)-2):
    if l[k]<l[j]:
        l[j],l[k]=l[k],l[j]
    if l[j]<l[i]:
        l[i],l[j]=l[j],l[i]
    j+=1
    k+=1
print(l)