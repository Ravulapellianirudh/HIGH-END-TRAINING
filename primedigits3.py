n=int(input()) 
while True:
    n1=n
    while n1>9:
        n1=sum(list(map(int,str(n1))))
    if n1 in [1,2,3,5,7]:
        print(n,n1)
        break
    else:
        n+=1 