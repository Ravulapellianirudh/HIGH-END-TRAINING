def rec(d,a):
    if int(a[:a.index(" ")])==1:
        d.add(a[a.index(" ")+1:])
    elif int(a[:a.index(" ")])==2:
        print(a[a.index(" ")+1:] in d)
    elif int(a[:a.index(" ")])==4:
        d.remove(a[a.index(" ")+1:])
    else:a
        s1=a[a.index(" ")+1:];f=0;c=0
        for i in d:
            s=''
            for j in i:
                s+=j
                if s==s1:
                    c+=1
                    break
        print(c)
n=9;d=set()
for i in range(n):
    a=input()
    rec(d,a)
