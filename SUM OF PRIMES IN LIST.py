l=[4,8,14,22,36,68]#sum of highest primes in a pair
j=1
a=0
def pr(n,c):
    if n==1 or n==2 or n==3:
        return 1
    elif n%c==0:    
        return 0
    elif n//2<=c:
        return 1
    else:
        return pr(n,c+1)
for i in range(len(l)-1):
    n=l[j]-1
    while True:
        if n>l[i] and pr(n,2):
            a+=n
            break
        elif n>l[i]:
            n-=1
        else:
            break
    j+=1
print(a)