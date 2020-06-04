class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = self.prev = self
    def __str__(self):
        return str(self.key)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        a = self.head.next
        while a:
            
            yield a
            a = a.next
        
    def __str__(self):
        return  "->".join(a for a in self)

    def __len__(self):
        return self.size

    def printList(self):
        h = self.head
        print("h","->",end=" ")
       
        h = h.next
        while h:
            if h.key == None:
                print("h")
                break
            else:
                print(h.key, "->", end=" ")
                h = h.next
    


    ################################################
    def splice(self,a,b,x):
        if a == None or b == None or x == None:
            return None
        
        ap = a.prev
        bn = b.next

        ap.next = bn
        bn.prev = ap

        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a

    def isEmpty(self):
            if self.size == None: return True
            else: return False
    def search(self, key):

        v = self.head.next
        while v:
            if v.key == key:
                return v
            else:
                v = v.next
                if v == self.head:
                    return None
    def moveAfter(self,a,x):
        self.splice(a,a,x)
    def moveBefore(self,a,x):
        #내부 함수 호출에서, self로 클래스 부터 호출해야 실행됨.
        #바로 함수이름쓰면 오류
        self.splice(a,a,x.prev)
        #인서트에는 
    def insertAfter(self,x,key):
        self.moveAfter(Node(key),x)
        self.size += 1
    def insertBefore(self,x,key):
        self.moveBefore(Node(key),x)
        self.size += 1
    def pushFront(self,key):
        self.insertAfter(self.head,key)
      
    def pushBack(self,key):
        self.insertBefore(self.head,key)
        
    def deleteNode(self,x):
        #x == self.head? 지우면 안됨.
        if x== None or x == self.head:
            
            return None
        #여기서 연결
        x.prev.next , x.next.prev = x.next , x.prev
        self.size -=1
    def popFront(self):
        #if self.isEmpty(): return None 안됨. 빈 노드 있음. 더미
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        #여기서 연결됨.
        self.deleteNode(self.head.next)
        
        return key
    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev
        self.deleteNode(self.head.prev)
        
        return key

    def first(self):
        if self.head.next == self.head: return None
        return self.head.next.key

    def last(self):
        if self.head.prev == self.head: return None
        return self.head.prev.key

#헤드에 더미 들어있는 거임.
#      

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
