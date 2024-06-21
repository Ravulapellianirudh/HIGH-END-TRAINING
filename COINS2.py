l=[1,3,4,5]
n=17
a=[999 for i in range(n+1)] 
for i in range(len(l)):
    for j in range(n+1):
        if j==l[i]:
            a[j]=1
        elif j<l[i] :
            a[j]=min(a[j],j)
        else:
            a[j]=min((j//l[i]+a[j%l[i]]),a[j])
print(a)