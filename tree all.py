class node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class atree:
    def __init__(self):
        self.root = None

    def creat(self, root, x):
        if root is None:
            return node(x)
        elif root.data > x:
            root.left = self.creat(root.left, x)
        else:
            root.right = self.creat(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def sumofroots(self, root):
        if root is None:
            return 0
        return root.data + self.sumofroots(root.left) + self.sumofroots(root.right)

    def sumofeven(self, root):
        if root is None:
            return 0
        if root.data % 2 == 0:
            return root.data + self.sumofeven(root.left) + self.sumofeven(root.right)
        else:
            return self.sumofeven(root.left) + self.sumofeven(root.right)

    def sumofodd(self, root):
        if root is None:
            return 0
        if root.data % 2 != 0:
            return root.data + self.sumofodd(root.left) + self.sumofodd(root.right)
        else:
            return self.sumofodd(root.left) + self.sumofodd(root.right)

    def height(self, root):
        if root is None:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

    def balance(self, root):
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return abs(left_height - right_height) <= 1 and self.balance(root.left) and self.balance(root.right)

    def leafnode(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.leafnode(root.left) + self.leafnode(root.right)

# Test the corrected code
t1 = atree()
t1.root = t1.creat(t1.root, 10)
t1.creat(t1.root, 20)
t1.creat(t1.root, 2)
t1.creat(t1.root, 7)
t1.creat(t1.root, 1)
t1.creat(t1.root, 3)
t1.creat(t1.root, 15)

print("inorder:", end=" ")
t1.inorder(t1.root)
print("\n")

print("preorder:", end=" ")
t1.preorder(t1.root)
print("\n")

print("postorder:", end=" ")
t1.postorder(t1.root)
print("\n")

print("sum of roots:", t1.sumofroots(t1.root))
print("sum of even root:", t1.sumofeven(t1.root))
print("sum of odd root:", t1.sumofodd(t1.root))
print("height of root:", t1.height(t1.root))
if t1.balance(t1.root):
    print("balance")
else:
    print("no")
print("leaf nodes:", t1.leafnode(t1.root))
