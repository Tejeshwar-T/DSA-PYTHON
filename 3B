class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            new_node.next = None
        else:
            new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {value}")


    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
            return
        temp = self.top
        self.top = self.top.next
        print(f"Popped: {temp.data}")
        del temp

 
    def display(self):
        if self.top is None:
            print("Stack is Empty!")
            return
        temp = self.top
        print("Stack elements (top to bottom):")
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = input("Enter value to push: ")
            stack.push(val)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
