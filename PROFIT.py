l=list(map(int,input().split(",")))
b=l[0];p=0
for i in range(len(l)):
    if b<l[i]:
        b=l[i]
    elif p<(l[i]-b):
        p=l[i]-b     