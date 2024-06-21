l = [13, 9, 4, 10, 5, 7]
def rec(l, i):
    if i >= len(l):5
        return 0
    c = l[i] + rec(l, i + 2)
    s = rec(l, i + 1)
    return max(c,s)
print(rec(l, 0))
