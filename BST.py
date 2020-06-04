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
            print(v.key,end=' ')
            self.inorder(v.right)
    def postorder(self, v):
       if v != None:
           self.postorder(v.left)
           self.postorder(v.right)
           print(v.key, end=' ')
    def find_loc(self, key):
       if self.size==0: return None
       p = None
       v = self.root
       while v:
           if v.key == key: return v
           else:
                if v.key < key:
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
       # key가 이미 트리에 있다면 에러 출력없이 None만 리턴!
        v = Node(key)
        if self.size ==0:
           self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key == key:
                return None
            elif p and p.key != key:
                if p.key < key: p.right = v
                else: p.left = v
                v.parent = p
                self.size += 1
                return v
T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        if v != None:
            print("+ {0} is set into H".format(v.key))
        else:
            print(key, "is already in the tree!")
    elif cmd[0] == 'search':
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
