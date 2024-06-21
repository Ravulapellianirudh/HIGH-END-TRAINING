s=input();s1=""#USING ASCII 
n=int(input())
for i in s:
    c=ord(i)
    while(n-26>0):
        n-=26
    if c>=97 and c<=122 and c-n<97:
        n=97-(c-n)
        s1+=chr(122-n)
    else:
        s1+=chr(c-n)
print(s1)
