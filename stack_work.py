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


	
def get_token_list(expr):
    token_list = []
    value =''
    for i in expr:
        if i.isdigit() or i is '.':
            value += i
        elif i is ' ':
            if value != '':
                token_list.append(value)
                value=''
        elif i in '()+-*/^':
            if value != '':
                token_list.append(value)
                value=''
            token_list.append(i)
        else:
            print("wrong input")
    if value != '':
        token_list.append(value)
    return " ".join(token_list)

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
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^':
            
            if(len(opstack.items) == 0):
                opstack.push(token)
            else:
                while(True):
                    if len(opstack) == 0:
                        opstack.push(token)
                        break
                    else:
                       
                        if prec[token] <= prec[opstack.top()]:
                            outstack.append(opstack.pop())
                        else:
                            opstack.push(token)
                            break
        else: # operand일 때
            outstack.append(token)
          

    while (len(opstack.items) != 0):
        outstack.append(opstack.pop())
    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    # ... ... ...
	
    return " ".join(outstack)

def compute_postfix(postfix):
    opstack = Stack()
    token_list = postfix.split(' ')
    
    while True:
        if(len(token_list) != 0):
            if(token_list[0] in "+-*/^"):
                second = float(opstack.pop())
                first = float(opstack.pop())
                computer = token_list.pop(0)
                if(computer == "+"):
                    opstack.push(first + second)
                elif(computer == "-"):
                    opstack.push(first - second)
                elif(computer == "*"):
                    opstack.push(first * second)
                elif(computer == "/"):
                    opstack.push(first / second)
                else:
                    opstack.push(first ** second)
            else:
                opstack.push(token_list.pop(0))
        else:
            break

    result = opstack.pop()
    return result

	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)