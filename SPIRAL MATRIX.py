def rec(i,j,l,n,c,a):
    if n==0:
        if j+c < len(l[0]):
            a.append(l[i][j])
            return rec(i,j+1,l,n,c,a)
        elif j+c==len(l[0]) and i+c==len(l):
            a.append(l[i][j])
            return a
        else:
            return rec(i+1,j-1,l,n+1,c,a)
    elif n==1:
        if i+c < len(l):
            a.append(l[i][j])
            return rec(i+1,j,l,n,c,a)
        elif i+c==len(l) and j<c:
            a.append(l[i][j])
            return a
        else:
            return rec(i-1,j-1,l,n+1,c,a)
    elif n==2:
        if j>=c:
            a.append(l[i][j])
            return rec(i,j-1,l,n,c,a)
        elif j<c and i<c :
            a.append(l[i][j])
            return a
        else:
            return rec(i-1,j+1,l,n+1,c+1,a)
    elif n==3:
        if i>=c:
            a.append(l[i][j])
            return rec(i-1,j,l,n,c,a)
        elif i<c and j+c==len(l[0]):
            a.append(l[i][j])
            return a
        else:
            return rec(i+1,j+1,l,0,c+1,a)
            
l=[[1,2,3],[4,5,6],[7,8,9]]
print(rec(0,0,l,0,0,[]))