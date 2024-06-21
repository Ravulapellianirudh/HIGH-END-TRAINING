class node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
        
class bst:
    def __init__(self):
        self.root=None
    def create(self,root,val):
        if root==None:
            return node(val)
        elif root.data>val:
            root.left=self.create(root.left,val)
        else:
            root.right=self.create(root.right,val)
        return root
    
    def left(self,temp,c,l):
        if temp==None:
            return
        if c not in l:
            l.append(c)
            print(temp.data)
        self.left(temp.left,c+1,l)
        self.left(temp.right,c+1,l)
    def right(self,temp,c,l):
        if temp==None:
            return
        if c not in l:
            l.append(c)
            print(temp.data)
        self.right(temp.right,c+1,l) 
        self.right(temp.left,c+1,l)
    def top(self,root):
        if not root:
            return 
        d={}
        q=[(root,0)]
        while():
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append(root.right,q[0][1]+1)
            if q[0][1] not in d:
                d.append(q[0][1])
            q.pop(0)
        for i in sorted(d):
            print(i)
    def height(self,temp,c):
        if not temp:
            return c
        return max(self.height(temp.right,c+1),self.height(temp.left,c+1))
    def leaf(self,temp):
        if not temp.right and not temp.left:
            print(temp.data,end=" ")
        if temp.left:
            self.leaf(temp.left)
        if temp.right:
            self.leaf(temp.right)
    def display(self,temp):
        if temp!=None:
            self.display(temp.left)
            print(temp.data,end=" ")
            self.display(temp.right)

t=bst()
t.root=t.create(t.root,11)
t.create(t.root,5)
t.create(t.root,15)
t.create(t.root,1)
t.create(t.root,6)
t.create(t.root,7)
t.create(t.root,8)
t.create(t.root,15)
t.display(t.root)
print("\nLEFT VIEW=")
t.left(t.root,0,[])
print("\n RIGHT VIEW=")
t.right(t.root,0,[])
print("\n TOP VIEW=")
t.top(t.root)
print("LEAF NODES=")
t.leaf(t.root)
print("\nHEIGHT=",t.height(t.root,0))
#absolute diff eo and add sum
#print all leaf nodes