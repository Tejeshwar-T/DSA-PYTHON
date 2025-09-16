class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def precedence(op):
   
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
   
    stack = Stack()
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  
        else:  
            while (not stack.is_empty() and
                   precedence(stack.peek()) >= precedence(char)):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)


if __name__ == "__main__":
    infix_expr = input("Enter an infix expression: ")
    postfix_expr = infix_to_postfix(infix_expr)
    print("Infix Expression: ", infix_expr)
    print("Postfix Expression: ", postfix_expr)

