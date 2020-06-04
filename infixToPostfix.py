'''
Infix to postfix
'''


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

def infix_to_postfix(infix):
    
    opstack = Stack()
    outstack = []
    token_list = infix.split(' ')

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
          opstack.push(token)
        elif token == ')':
            while(opstack.top() != "("):
                token = opstack.pop()
                if(token == "("):
                    continue
                else:
                    outstack.append(token)
         
        elif token in '+-/*^':
            
            if len(opstack) == 0:
                outstack.append(token)
            elif len(opstack) != 0:
                while True:
                    if len(opstack) == 0:
                        outstack.append(token)
                        break
                    else:
                        if prec[token] <= prec[opstack.top()]:
                            outstack.append(opstack.pop())
                        else:
                            opstack.push(token)
                            break
        else: # operand일 때
            outstack.append(token)
          

    while not opstack.isEmpty():
        outstack.append(opstack.pop())
    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    # ... ... ...
	
    return " ".join(outstack)


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)
