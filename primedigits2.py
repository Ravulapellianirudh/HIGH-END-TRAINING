def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return 1
    return 0
n=int(input())
while True:
    l=list(map(int,str(n)))
    while True:
        if len(l)!=1:
            n1=sum(l)
            l=list(map(int,str(n1)))
        else:
            break
    if prime(n1)==0:
        print(n)
        break
    else:
        n+=1
            