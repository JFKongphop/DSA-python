# Single Linked List** − Item navigation is forward only.
# can add the new list only at the tail of linked list

#Linked List Exercise 1: Singly Linked Lists

# collect the data each node
class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

    
class SingleLinkedList:
    # set the first node  
    def __init__(self, value) -> None:
        self.head = Node(value)

    # insert at the last position of linkedList
    def insert(self, value):
        current = self.head

        # move the current of node
        while current.next is not None:
            current = current.next
        
        # set new node after insert it at last position like push in array
        current.next = Node(value)

    # delete by get the value and check it is valid
    def delete(self, value):
        # not found in linkedList
        if self.search(value) is not True:
            return 'Not in list'
        
        else:
            current = self.head
            while current is not None:
                # found the value then cut this node and reconnect to next of this node
                # node1 => node2 cut it out => node3 | then is node1 => node2
                if current.next.value == value:
                    current.next = current.next.next
                    break
                
                # find next one if not found
                else:
                    current = current.next
        
    # start with tail to head
    def reverse(self):
        current = self.head
        # set the initial value for temp
        previous , next = None, None
        
        # tem all of positions with loop
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous
            
    # search in the node that have the value or not and return boolean
    def search(self, value):
        current = self.head
        while current is not None:

            # find ah the first position
            if current.value == value:
                return True

            # find next one if not found
            else:
                current = current.next
            
        return False

    # show of all element in linkedList
    def display(self):
        current = self.head
        
        # check current is valid
        while current is not None:
            # then stop in tails is None
            if current.value is not None:
                print(current.value, end = ' ')
            
            # set the next value to print in looping again
            current = current.next

        print()

sll = SingleLinkedList(None)
sll.insert("Python")
sll.display()
sll.insert(20)
sll.display()
sll.insert(30)
sll.display()
sll.delete("Python")
sll.display()
sll.insert(10)
sll.display()
sll.insert(30)
sll.insert(60)
sll.display()
sll.delete(30)
sll.display()
sll.insert(90)
sll.display()
sll.reverse()
sll.display()
sll.search(30)
sll.insert("Python")
sll.display()