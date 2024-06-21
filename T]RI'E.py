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
        return True
    
                
            
tr=trie()
tr.insert('abcd')
print(tr.search('abc'))
tr.insert('apple')
tr.insert('ape')
print(tr.search('apple'))
print(tr.search('ape'))