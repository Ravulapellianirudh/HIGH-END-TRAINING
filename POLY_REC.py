def pol(n,s):
    if n==0:
        return s
    else:
        r=n%10
        s=s*10+r
        return pol(n//10,s)
n=int(input())
n1=pol(n,0)
if n==n1:
    print("YASSSS")
else:
    print("NOOOOO")