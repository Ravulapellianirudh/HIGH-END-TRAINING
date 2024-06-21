def rec(g,n,v):
    if v[n-1]==0:
        l.append(n)
        v[n-1]=1
    if 0 not in v:
            a.extendGRAP(l)
        l.pop()
    for i in g[n]:
        if v[i-1]==0:
            rec(g,i,v)
g={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],8:[3,4,2],2:[4,8]}
v=[0]*max(g.keys())
l=[]
a=[]
rec(g,list(g.keys())[0],v)
print(l,a)