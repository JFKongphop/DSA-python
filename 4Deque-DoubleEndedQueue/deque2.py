#Deque Exercise 2: Creating Deque and Deque Operations 2
#index(), insert(), remove(), count() 
#Imporing "Collections" for deque operations

import collections 
deque = collections.deque([1, 2, 3, 3, 4, 2, 4])

print(deque)
# find the index in deque
print(deque.index(4, 2, 5)) # element, start, end of position

# insert => index, argument
deque.insert(4, 6)
print(deque)

# count specifix element
print(deque.count(3))

# remove element
print(deque.remove(6))