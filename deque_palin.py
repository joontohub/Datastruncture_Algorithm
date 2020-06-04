class Deque:
    items = []
    def __init__(self,s):
        
        for i in s:
            self.items.append(i)
        
    def append(self,c):
        self.items[0] = c
        return self.items[0]
    
    def appendleft(self,c):
        return self.items.append(c)

    def pop(self):
        return self.items.pop(0)
    def popLeft(self):
        return self.items.pop()
    def __len__(self):
        return len(self.items)
    def right(self):
        return self.items[0]
    def left(self):
        return  self.items[-1]

def check_palindrome(s):
    dq = Deque(s)

    palindrome = True

    while len(dq)> 1:
      
        if dq.popLeft() != dq.pop():
            
            palindrome = False
    
    print(palindrome)

s = input()
check_palindrome(s)