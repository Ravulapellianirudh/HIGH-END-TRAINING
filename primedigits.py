def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 1
    return 0
n=123456789
print("PRIMES:");c=0
while n!=0:
    a=n%10
    if prime(a)==0:
        print(a)
        c+=1
    n//=10
    
print('COUNT=',c)
##############

n=123456789
c=0
while(n!=0):
    if (n%10 in [1,2,3,5,7]):
        c+=1
    n//=10
print(c)
