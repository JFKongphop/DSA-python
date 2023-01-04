#Queue Exercise 3  Creating Queue Class for Calling enqueue() and dequeue()

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        
        return None

    def size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue('Kongphop')
queue.enqueue('Hate')
queue.enqueue('Python')
print(queue.size())

queue.dequeue()
print(queue.queue)