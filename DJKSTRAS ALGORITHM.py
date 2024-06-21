def minpath(g,d,l,l1):
    if not l1:
        print(l)
        return d
        
    l.append(l1[0])
    for i in g[l1[0]]:
        if i[0] not in l:
            if d[i[0]]>i[1]+d[l1[0]]:
                
                d[i[0]]=i[1]+d[l1[0]]
            l1.append(i[0])
    l1.pop(0)
    d=minpath(g,d,l,l1)
    return d
g={5:[(7,3),(3,2)],7:[(5,3),(4,6),(3,4)],4:[(7,6),(8,1),(2,2)],3:[(5,2),(7,4),(8,5)],8:[(3,5),(4,1),(2,3)],2:[(4,2),(8,3)]}
d={5:0,7:999,4:999,3:999,8:999,2:999}
print(minpath(g,d,[],[list(g.keys())[0]]))