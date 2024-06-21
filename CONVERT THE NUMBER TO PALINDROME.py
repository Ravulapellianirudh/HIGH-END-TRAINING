l=list(map(int,str(76583)))
if len(l)%2==0:
    m=len(l)//2 
else:
    m=len(l)//2 +1
for i,j in zip(range(len(l)//2-1,-1,-1),range(m,len(l),1)):
    if l[i]==l[j] and j==m and i+2!=j:
        l[i]+=1
        l[j]+=1
    elif l[i]<l[j] and j==m and i+2!=j:
        l[i]=l[j]
    elif l[i]<=l[j] and j==m :
        l[i+1]+=1
        l[j]=l[i]
    elif l[i]==l[j]:
        continue
    else:
        l[j]=l[i]
print("".join(map(str,l)))
    #INPUTS=24,1112,11112,76583,56472,1234,122