def lo(s,p):
    l=[]
    for i in s:
        l.append(p.index(i))
    l.sort();s=''
    for i in l:
        s+=p[i]
    print(s)
n=int(input())
for i in range(n):
    p=input()
    s=input()
    lo(s,p)   
    
#input1:
    #polikujmnhytgbvfredcxswqaz
    #abcd
    #bdca 
#input2:
    #qwryupcsfoghjkldezxvbintma
    #ativedoc
    #codevita
