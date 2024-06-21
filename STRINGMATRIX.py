n=int(input());l=[list(input()) for _ in range(n)];c=0
s=input()
for i in s:
    if c==n:
        c=0
    if i not in l[c]:
        print("NO")
        break
    c+=1    
else:
    print("YESSS")