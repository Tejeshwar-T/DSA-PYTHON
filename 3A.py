class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, book):
        if self.is_full():
            print("Stack is full! Cannot push.")
        else:
            self.top += 1
            self.stack[self.top] = book
            print(f'"{book}" added to stack.')

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
        else:
            book = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f'"{book}" removed from stack.')

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print(f'Top of stack: "{self.stack[self.top]}"')


# Example usage
s = Stack(5)
s.push("Book A")
s.push("Book B")
s.peek()
s.pop()
s.peek()
