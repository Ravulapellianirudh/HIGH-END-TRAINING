def valid (b,i,j):
    if (b[i][j] in b[i][j+1:] or b[i][j] in b[i][:j] )and b[i][j]!='.':
        print(b[i][j],b[i][j+1:],b[i][:j])
        return False
    for k in range(len(b)):
        if i!=k and b[k][j]==b[i][j]:
            print(b[i][j],b[i][j+1:],b[i][:j])
            return False
    return True
b = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
f=1
for i in range(len(b)-1):
    for j in range(len(b)):
        if not valid(b,i,j):
            print(False)
            f=0
            break
    if not f:
        break
else:
    print(True)