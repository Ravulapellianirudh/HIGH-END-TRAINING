def rec(i,j,l,s,a,k1,k2):
    if i==len(l)-1 and j==len(l[0])-1:
        s.append(l[i][j])
        a.append(s.copy())
        s.pop()
        return a 
    if j<len(l[0])-1:
        if l[i][j]!=k1 and l[i][j]!=k2:
            s.append(l[i][j])
            rec(i,j+1,l,s,a,k1,k2)
            s.pop()
        else:
            return
    if i<len(l)-1:
        if l[i][j]!=k1 and l[i][j]!=k2:
            s.append(l[i][j])
            rec(i+1,j,l,s,a,k1,k2)
            s.pop()
        else:
            return
    return a
def re(i,j,l,s,a):
    if i==len(l)-1 and j==len(l[0])-1:
        s.append(l[i][j])
        a.append(s.copy())
        s.pop()
        return a
    if j<len(l[0])-1:
        s.append(l[i][j])
        re(i,j+1,l,s,a)
        s.pop()
    if i<len(l)-1:
        s.append(l[i][j])
        re(i+1,j,l,s,a)
        s.pop()
    return a
l=[[1,2,3],[4,5,6],[7,8,9]]
print("ALL PATHS=\n","\n".join(map(str,re(0,0,l,[],[]))))
print("SELECTIVE PATHS=\n","\n".join(map(str,rec(0,0,l,[],[],3,4))))