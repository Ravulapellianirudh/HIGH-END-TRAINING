class node:
    def __init__(self):
        self.d={}
        self.f=0
        self.c=0
class trie:
    def __init__(self):
        self.root=node()
    def insert(self,word):
        t=self.root
        for i in word:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.f=1
        
    def search(self,s):
        t=self.root
        for i in s:
            if i in t.d.keys():
                t=t.d[i]
            else:
                return False
        return t.f==1
    
    def prefix(self,s):
        t=self.root
        for i in s:
            if i in t.d.keys():
                t=t.d[i]
            else:
                return False
        return True
    
    def pre(self,a,m):#PRINT PREFIX WITH LONGEST SUBSTRING 
        if a:           #IF EQUAL CHECK LEXOGRAPHICALLY SMALL
            m=a[0];m1=0
            for i in a:
                n=self.sug([],self.root,i)
                if m1==max(n) and ord(i[0])<ord(m[0]):
                    m=i
                elif max(n)>m1:
                    m1=max(n)
                    m=i
                
        return m
    
    def sug(self,l,t,s):
        for i in s:
            if i in t.d:    
                t=t.d[i]
            else:
                return [0]
        l1=list(s)
        def rec(t,s,l,l1):
            if t.f==1 and t.d!=None:
                l.append(len(l1))
            elif t.f==1:
                l.append(len(l1))
                return
            for i in t.d:
                l1.append(i)
                rec(t.d[i],s,l,l1)
                l1.pop()
        rec(t,s,l,l1)
        return l
    
    def sug_words(self,l,t,s):#SUGGEST ALL WORDS FOR A PREFIXES
        for i in s:
            t=t.d[i]
        l1=list(s)
        def rec(t,s,l,l1):
            if t.f==1 and t.d!=None:
                l.append("".join(l1))
            elif t.f==1:
                l.append("".join(l1))
                return
            for i in t.d:
                l1.append(i)
                rec(t.d[i],s,l,l1)
                l1.pop()
        rec(t,s,l,l1)
        return l
    def sug_pre(self,l,t,s):#SUGGEST ALL POSSIBLE PREIXES OF A PREFIX
        for i in s:
            t=t.d[i]
        l1=list(s)
        l.append("".join(l1))
        def rec(t,s,l,l1):
            if t.f==1 and t.d==None:
                return
            for i in t.d:
                l1.append(i)
                l.append("".join(l1))
                rec(t.d[i],s,l,l1)
                l1.pop()
        rec(t,s,l,l1)
        return l
            
tr=trie()
tr.insert('wood')
tr.insert('world')
tr.insert('word')
tr.insert('words')
tr.insert('wore')
tr.insert('abcd')
print(tr.search('abcd'))
tr.insert('apple')
tr.insert('ape')
print(tr.search('appl'))
print(tr.prefix('appl'))
print(tr.search('ape'))
print(tr.sug_words([],tr.root,'wo'))
print(tr.sug_pre([],tr.root,'ap'))
print(tr.pre(['b','ba','wo','ap'],"no prefixes present"))