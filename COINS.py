l=[1,3,4,5]
n=17
a=[[] for i in range(max(l)+1)] 
for i in range(len(l)):
    for j in range(n+1):
        if j==l[i]:
            a[l[i]].append(1)
        elif j<=l[i] and l.index(l[i])==0:
            a[l[i]].append(j)
        elif l.index(l[i])==0:
            a[l[i]].append(j//l[i] + j%l[i])
        elif j<l[i] :
            a[l[i]].append(a[l[i-1]][j])    
        else:
            a[l[i]].append(min((j//l[i]+a[l[i-1]][j%l[i]]),a[l[i-1]][j]))
print("\n".join(map(str,a)))