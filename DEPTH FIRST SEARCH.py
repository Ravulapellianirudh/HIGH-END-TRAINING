def nodes(g,n,l): #ALL POSIIBLE NODES
    l.append(n)
    for i in g[n]:
        if i[0] not in l:
            nodes(g,i[0],l)
    return l

def path(g,n,l): #ALL POSSIBLE TRAVERSAL PATHS
    l.append(n)
    print(l)
    if n==list(g.keys())[len(list(g.keys()))-1]:
        print(l)
        l.pop()
        return
    for i in g[n]:
        if i[0] not in l:
            path(g,i[0],l)
    l.pop()
    
def mincost(g,n,l,s,m,l1): #MINIMUM COST TO TRAVERSE
    l.append(n)
    if n==list(g.keys())[len(list(g.keys()))-1]:
        if s<=m:
            m=s
            l1=l.copy()
        l.pop()
        return m,l1
    for i in g[n]:
        if i[0] not in l:
            m,l1=mincost(g,i[0],l,s+i[1],m,l1)
    l.pop()    
    return m,l1

def minpath(g,n,l,s,a): #MINIMUM PATH TO TRAVERSE
    l.append(n)
    if n==list(g.keys())[len(list(g.keys()))-1]:
        a[s]=l.copy()
        l.pop()
        return 
    for i in g[n]:
        if i[0] not in l:
            s+=i[1]
            minpath(g,i[0],l,s,a)
            s-=i[1]
    l.pop()    
    return a

g={5:[(7,3),(3,2)],7:[(5,3),(4,6),(3,4)],4:[(7,6),(8,1),(2,2)],3:[(5,2),(7,4),(8,5)],8:[(3,5),(4,1),(2,3)],2:[(4,2),(8,3)]}
print("NODES=",nodes(g,list(g.keys())[0],[]))
print("ALL POSSIBLE WAYS TO TRAVERSE:")
path(g,list(g.keys())[0],[])
print("MINIMUM COST=",mincost(g,list(g.keys())[0],[],0,999,[]))
print("MINIMUM PATH=",minpath(g,list(g.keys())[0],[],0,{})[min(list(minpath(g,list(g.keys())[0],[],0,{}).keys()))])

