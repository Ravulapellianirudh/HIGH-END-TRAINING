n=int(input())
def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 1
    return 0
while True:
    if n%2==0 and n!=2:
        n+=1
    elif prime(n)==0:
        break
    else:
        n+=1
print(n)

