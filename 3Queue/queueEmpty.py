#Queue Exercise 1: Creating Stack using list Built-in --> queue = Empty
# first in first out

queue = []
queue.append(555) # append = enqueue
queue.append('python')
queue.append('programming')
print(queue)

queue.pop(0) # pop(0) delete index 0 is dequeue
print(queue)