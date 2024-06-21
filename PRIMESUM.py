n=int(input("Enter a number:"))
def pr(n,c):
    if n==1 or n==2 or n==3:
        return 1
    elif not n%c:
        return 0
    elif n//2==c:
        return 1
    else:
        pr(n,c+1)
def fun(i,j,n):
    if pr(i,2) and pr(j,2):
        print("YES")
        return
    elif i==j or i==j-1:
        print("NO")
        return
    else:
        fun(i+1,j-1,n)
fun(1,n-1,n)