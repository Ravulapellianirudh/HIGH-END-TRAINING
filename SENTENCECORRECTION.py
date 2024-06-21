l=list(input().split(" "))
a=["" for i in range(len(l))]
for i in l:
    a[int(i[-1])-1]+=i[:-1]
print(" ".join(a))