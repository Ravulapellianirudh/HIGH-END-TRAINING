for i in range(300,401):
    if i%7==0:
        print(i)
n1=300
n=300+(7-(n1%7))
while n<401:
    print(n)
    n+=7
print(abs((300//7)-(400//7)))