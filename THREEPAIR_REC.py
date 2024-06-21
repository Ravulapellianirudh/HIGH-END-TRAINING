def rec(l,i,j,k,c):
    if c==0 and k<len(l)-1:
        print(l[i],l[j],l[k])
        rec(l,i,j,k+1,0)
    elif c==1 and j<len(l)-2:
        print(l[i],l[j],l[k])
        rec(l,i,j+1,k,1)
    elif c==0 and k==len(l)-1 and i<len(l)-3:
        print(l[i],l[j],l[k])
        rec(l,i+1,i+2,i+3,0)
    else:
        print(l[i],l[j],l[k])
l=[1,2,3,4,5,6,7,8]
rec(l,0,1,2,0)