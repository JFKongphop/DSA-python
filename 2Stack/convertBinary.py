#Stack Exercise 5: Coverting Decimal Numbers to Binary Numbers Using Stacks

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

numberDec = 0
numberBin = '' 
numberDec = int(input("Please enter the integer to covert: "))

DecToBinStack = Stack()

while numberDec > 0:
    DecToBinStack.push(numberDec % 2)
    numberDec = numberDec // 2 # get only interger not get remainder from division

while DecToBinStack.isEmpty() == False:
    numberBin += str(DecToBinStack.pop()) # get last element to get the binary

print(numberBin)