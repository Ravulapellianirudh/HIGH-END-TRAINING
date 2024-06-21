n=int(input())
l=[0,5,3,6,7,2,1];j=n
for i in range(n//2 +1):
    if i not in l:
        print(i)
        break
    elif j not in l:
        print(j)
        break
    else:
        j-=1