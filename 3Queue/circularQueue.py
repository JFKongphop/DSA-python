#Queue Exercise 4 Circular Queue Implementation
# set the size of circular and set each index with none or null to prepare the queue to enqueue
# first and last is the same position
class CircularQueue():
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        # if it return the same number (-1) that inform about the queue is full
        # becuse it return to the same index of queue
        if (self.rear + 1) % (self.size) == self.front:
            print('Queue is full')

        # queue is empty not have element in queue
        # enqueue it in the first of queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.front] = data 
        
        # queue is have some element before
        # enqueue next position
        else:
            # mod the last to be start new next position (2 % 5 == position 2)
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        # check empty queue
        # starting position is not change
        if self.front == -1:
            print('Queue is empty')
        
        # queue have only one element
        elif self.front == self.rear:
            # get the one element at first position
            temp = self.queue[self.front]
            # clear to initial value
            self.front = -1
            self.rear = -1

            return [temp, "elif"]

        # queue have multiple elements
        # return of the queue
        else:
            temp = self.queue[self.front]

            # get back to initial position 
            self.front = (self.front + 1) % self.size
            return [temp, "else"]

        
    def display(self):
        # check empty queue
        if self.front == -1:
            print('Queue is empty')
        
        # the last position is move from -1 that is queue is not empty
        elif self.rear >= self.front:
            print('ELIF Element in the circular queue are : ', end = "")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            
            print()
            
        # print all element
        else:
            print('ELSE Element in the circular queue : ', end = "")
            # get element in front position to index of size
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            
            print()
        
        # check queue is full
        # queue postion circulate back to front
        if (self.rear + 1) % self.size == self.front:
            print('Queue is full')


# create queue
# size 5
queue = CircularQueue(5)
print(queue.queue)
queue.enqueue(14)
queue.display()
queue.enqueue(22)
queue.display()
queue.enqueue(13)
queue.display()
queue.enqueue(-6)
queue.display()

# dequeue
# remove first position
print('Deqeue from first position : ', queue.dequeue())
queue.display()
print('Deqeue from first position : ', queue.dequeue())
queue.display()

queue.enqueue(9)
queue.enqueue(20)
queue.enqueue(5)
queue.display()
queue.enqueue(5)

print(queue.queue)