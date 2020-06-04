# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
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

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = None
        p = self.find_loc(key)
        if p == None:
            v = self.root= Node(key)
        elif p.key != key:
            v = Node(key)
            v.parent = p
            if p.key > key:
                p.left = v
            else:
                p.right = v
        if v != None:
            self.size = self.size + 1
        return v

class SplayTree(Tree):

    def right_rotate(self, x):
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

    def left_rotate(self, x):
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


    def splay(self, x):
        if not x: return None
        if x == self.root: return x
        while x != self.root:
            if x == x.parent.left:
                self.right_rotate(x.parent)
            elif x == x.parent.right:
                self.left_rotate(x.parent)
        return x

    def search(self, key):
        v = super(SplayTree,self).search(key)
        if v:
            self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(SplayTree,self).insert(key)
        self.root = self.splay(v)
        return v
    
    def delete(self, x):
        self.splay(x)
        L, R = x.left, x.right

        if L != None:
            m = L
            while m.right:
                m = m.right
            self.splay(m)
            m.right = None
            m.right = R
            R.parent = m
        if L == None:
            if R:
                R.parent = None
                self.root = R
            else:
                if x == self.root:
                    del x
                    self.root = None

    def preorder(self, v):
        super(SplayTree, self).preorder(v)

    def postorder(self, v):
        super(SplayTree, self).postorder(v)

    def inorder(self, v):
        super(SplayTree, self).inorder(v)

T = SplayTree()

while True:
    cmd = input().split()
    if cmd[0] == 'in':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'del':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'find':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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
