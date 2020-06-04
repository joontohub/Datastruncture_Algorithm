class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)
    def inorder(self,v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self,v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')
    def find_loc(self, key):
        if self.size == 0: return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        
        return p
    def search(self,key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None
    
    def insert(self,key):
        v = Node(key)
        if self.size == 0:
            self.root = v
            self.size += 1
            return v
        else:
            p = self.find_loc(key)
            
            if p and p.key == key:
                return None
            elif p and p.key != key:
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
                self.size += 1
                return v
    def deleteByMerging(self,x):
        a,b, pt = x.left , x.right, x.parent
        if a == None: c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m
        if self.root == x:
            if c: c.parent = None
            self.root = c
        else:
            if pt.left == x: pt.left = c
            else: pt.right = c
            if c: c.parent = pt
        self.size -= 1

    def deleteByCopying(self,x):
        if x == None: return None
        a = x.left
        if a == None:
            b, pt = x.right, x.parent
            if pt == None:
                self.root = b
            else:
                if pt.left == x: pt.left = b
                else: pt.right = b
            if b: b.parent = pt

        else:
            m = a
            while m.right:
                m = m.right
            x.key = m.key
            l, pt = m.left, m.parent
            if pt.left == m:
                pt.left = l
            else:
                pt.right = l
            if l:
                l.parent = pt
            del m
        self.size -= 1

    def height(self, x):
        if x == None: return -1
        else:
            a = self.height(x.left)
            b = self.height(x.right)
            if a > b:
                return a + 1
            else:
                return b + 1

    def number(self, x):
        if x == None: return 0
        else:
            a = self.number(x.left)
            b = self.number(x.right)
            return a + b + 1
    def rotateLeft(self, x):
        if not x: return None
        z = x.right
        if z== None: return None
        b = z.left
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        if x:
            z.left = x
        x.parent = z
        x.right = b
        if b: b.parent = x
        if x == self.root:
            self.root = z

    def rotateRight(self, x):
        if not x: return None
        a = x.left
        if a == None: return None
        b = a.right
        a.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = a
            else:
                x.parent.right = a
        if a:
            a.right = x
        x.parent = a
        x.left = b
        if b: b.parent = x
        if x == self.root:
            self.root = a

T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'number':
        num = T.number(T.search(int(cmd[1])))
        if num == 0:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has {1} descendants".format(cmd[1], num))
    elif cmd[0] == 'Rleft':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(z)
            print(" * Rotated left at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
    elif cmd[0] == 'Rright':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(z)
            print(" * Rotated right at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
