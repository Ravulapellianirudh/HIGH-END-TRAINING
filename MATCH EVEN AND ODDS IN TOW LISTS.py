def rec(l,l1,a,i,s):
    if i==len(l):
        return a,s
    def r(l1,n,j,m):
        if j==len(l1):
            return m
        if l1[j]%2!=0:
            m.append(n+l1[j])
        return r(l1,n,j+1,m)
    if l[i]%2==0:
        a.extend(r(l1,l[i],0,[]))# MATCH EVENS OF LIST 1 WITH ODDS OF LIST 2
        s.append(sum(r(l1,l[i],0,[])))#SUM OF EACH MATCHED LIST
    return rec(l,l1,a,i+1,s)
l=[6,3,2,9,4,7] 
l1=[8,7,5,3,6,9]
print(" \n".join(map(str,rec(l,l1,[],0,[]))))