dictionary = ["cat","bat","rat"]
l=['the','cattle','was','rattled','by','the','battery']
for i in l:
    s=""
    for j in i:
        s+=j
        print(s,i,dictionary)
        if s in dictionary:
            c=l.index(i)
            l[c]=s
print(" ".join(l))
