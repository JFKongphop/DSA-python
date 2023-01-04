#Deque Exercise 3: Creating Deque and Deque Operations 3 
#extend(), extendleft(), rotate(), reverse() 
#Importing "Collections" for deque operations

import collections

deque = collections.deque([1, 2, 3])
print(deque)

deque.extend([4, 5, 6])
print(deque)

deque.extendleft([7, 8, 9])
print(deque)

# move last poistion to first position
deque.rotate()
print(deque)

# rotatae by lenght
deque.rotate(-3)
print(deque)

# reverse
deque.reverse()
print(deque)
