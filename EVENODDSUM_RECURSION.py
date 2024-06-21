l1=list(map(int,input().split(",")))
l2=list(map(int,input().split(",")))
print(l1,l2)
def fn(l1,l2):
    def ev(l1,i1,s1):
        if i1<len(l1):
            if l1[i1]%2==0:
                s1+=l1[i1]
            print(l1,i1,s1)
            i1+=1
            a=ev(l1,i1,s1)
        else:
            a=s1
            return s1
        return a
    def od(l2,i1,s1):
        if i1<len(l2):
            if l2[i1]%2!=0:
                s1+=l2[i1]
            print(l2,i1,s1)
            i1+=1
            a=od(l2,i1,s1)
        else:
            a=s1
            return s1
        return a
    a=ev(l1,0,0)
    b=od(l2,0,0)
    print(a,b)
fn(l1,l2)