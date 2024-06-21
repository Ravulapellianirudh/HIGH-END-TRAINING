def rec(l):
    print(l)
    if len(l)!=4:
        l.append(l)
        rec(l)
    print(l)