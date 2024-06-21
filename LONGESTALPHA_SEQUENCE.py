s=input();c=0;m=0
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        c+=1
    elif c>m:
        m=c
        c=1
    else:
        c=1
if m==0 and c>0:
    m=c+1
print(m)
        