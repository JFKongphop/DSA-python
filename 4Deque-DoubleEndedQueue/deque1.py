#Deque Exercise 1: Creating Deque and Deque Operations 1
#append(), appendleft(), pop(), and popleft() 
#Importing "collections" for deque operations

import collections
deque = collections.deque([11, 3, 9])

print(deque)

deque.append(4)
print(deque)
deque.appendleft(5)
print(deque)

deque.pop()
print(deque)
deque.popleft()
print(deque)