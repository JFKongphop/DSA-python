#Stack Exercise 4: Python Stack Implementation --> Creating Stack Class for Calling push() and pop()

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items = self.items[:len(self.items) - 1]

    def top(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


stack = Stack()
stack.push('1')
stack.push('2')
print(stack.size())
stack.pop()
print(stack.size())
print(stack.top())
print(stack.pop())
print(stack.isEmpty())