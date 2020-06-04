class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1] 
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def compute_postfix(postfix):
    opstack = Stack()
    token_list = postfix.split(' ')
    
    while True:
        if(len(token_list) != 0):
            if(token_list[0] in "+-*/"):
                first = float(opstack.pop())
                second = float(opstack.pop())
                computer = token_list.pop(0)
                if(computer == "+"):
                    opstack.push(first + second)
                elif(computer == "-"):
                    opstack.push(first - second)
                elif(computer == "*"):
                    opstack.push(second * first)
                else:
                    opstack.push(second / first)
            else:
                opstack.push(token_list.pop(0))
        else:
            break

    result = ("%0.4f" %opstack.pop())
    return result

postfix = input()
result = compute_postfix(postfix)
print(result)