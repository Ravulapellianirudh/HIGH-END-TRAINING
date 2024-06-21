def q(n):
    def s(b,r,c):
        for i in range(0,r):
            if b[i][c]:
                return False
        for i in range(0,c):
            if b[r][i]:
                return False
        i=r-1
        j=c-1
        while(i>=0 and j>=0 and  j<=len(b[0])):
            if b[i][j]==1:
                return False
            i-=1
            j-=1
        i=r-1
        j=c+1
        while(i>=0 and j<len(b[0]) and j>=0):
            if b[i][j]==1:
                return False
            i-=1
            j+=1
        return True
    def sol(b,r,re):
        if len(b)==r:
            re.append([i[:] for i in b])
            return re
        else:
            for c in range(len(b[r])):
                if s(b,r,c):
                    b[r][c]=1
                    re=sol(b,r+1,re)
                    b[r][c]=0
            return re
                
                     
    b=[[0 for i in range(n)]for j in range(n)]
    return sol(b,0,[])
n=5
s=q(n)
for i in s:
    for j in i:
        print(" ".join('Q' if k==1 else '-' for k in j))
    print()
print(len(s))