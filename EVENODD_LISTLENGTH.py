l=list(map(int,input().split(",")))
i=0;j=-1
while True:
    if id(l[i])==id(l[j]):
        print("ODD")
        break
    elif id(l[i+1])==id(l[j]):
        print("EVEN");break
    else:
        i+=1
        j-=1