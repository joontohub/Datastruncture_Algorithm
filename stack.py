class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return
    def __len__(self):
        return len(self.items)



n , k = input().split()
n = int(n)
k = int(k)

count = 0
Val_list = []
stack = Stack()

number = input() + ' '
word = ''
for i in number:
  if i == ' ':
    Val_list.append(word)
    word = ''
  else:
    word += i
    

while len(Val_list) != 1:
  for i in range(k):
    if len(Val_list) != 0:
      a = Val_list.pop(0)
      stack.push(a)
  count += 1
  small = stack.pop()
  while len(stack) != 0: 
    second = stack.pop()
    if second < small:
      small = second
  Val_list.insert(0,small)
  
print(count)