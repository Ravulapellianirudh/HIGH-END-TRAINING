l=[2,3,5,6]
n=11
t=[0 for i in range(n+1)] 
t[0]=1
for i in range(len(l)):
    for j in range(n,l[i]-1,-1):
        if t[j-l[i]]:
            t[j]=1
if t[n]:
    print(True)
else:
    print(True)