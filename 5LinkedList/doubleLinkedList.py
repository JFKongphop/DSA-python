#Doubly Linked List − Items can be navigated forward and backward.
# can insert the data between the node in list but cannot insert before of the position of linikedList
#Linked List Exercise 2: Doubly Linked Lists

#If no head, set new node as head

    #if next not none (tail) continue traversing

    #if tail, add to end
    
    #set prev pointer to current node
    
    #set new tail to new node
    
    #Create new node

    #If val is first item in list, insert after 
    
    #If tail is val, create new tail

        #If neither head nor tail, traverse through
    
            #If val is not in list, give error message
        
        #Set new node's next to current node's next 
    
        #Insert new node next to current node
    
        #Set new node next prev's pointer to new node

        #Set new node's prev pointer to current node 
    


    #If val is the head 

    #If val is the tail

            #If val is not in list 
    
        #Set next next node's prev pointer to current node
    
        #Set next node to current's next next pointer
    
#Create empty list

    #Start at head and check if next is not tail

        #Add current node to list and traverse forward
			
class Node(object): 
	def __init__(self, value): 
		self.value = value 
		self.next = None 
		self.prev = None

class DoubleLinkedList(object):
    # set head and tail of DoubleLinkedList
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # add it at last position (tail)
    def addNode(self, value):
        # create new node and preparing to insert to doubleLinkedList
        newNode = Node(value)

        # doubleLinkedList is empty set it to head and tail
        if self.head == None:
            self.head = newNode
            self.tail = newNode

        # move of the next position because it not empty
        else:
            # set of the initial of node
            currentNode = self.head

            # find the tail that the value is None
            while currentNode.next != None:
                currentNode = currentNode.next

            # when detect tail set the node to the last position
            currentNode.next = newNode
            
            # set the pointer to point it at the latest node before it adding
            newNode.prev = currentNode
            
            # set the new node at the last position (tail)
            self.tail = newNode


    # get the value if the node and insert it after this value
    def insertNodeAfter(self, value, insertValue):
        
        # check doubleLinkedList is empty
        if self.head != None:
            currentNode = self.head 

            #create new node
            newNode = Node(insertValue)

            # if inseetValue is first item is doubleLinkedList insert it after head(None)
            if self.head.value == value:
                
                # set new node in doubleLinkedList
                self.head.next.prev = newNode
                
                # set pointer to point the lastest before this node but in this situation the fist is head that point to None
                newNode.prev = self.head
                
                # set the next pointer
                newNode.next = self.head.next
                
                # set the next position of head
                self.head.next = newNode

            
            # if the insertValue at the last position (tail)
            elif self.tail.value == value:
                
                # insert it after the this postion that want to insert
                self.tail.next = newNode
                
                # set pointer to point the previos node
                newNode.prev = self.tail
                
                # create new node
                self.tail = newNode
            
            # if the position that want to insert is between the head and tail
            else:
                # find the position of the val that want to insert
                while currentNode.value != value:
                    
                    # set the next node to find the position
                    currentNode = currentNode.next 
                    
                    # move the next one to find the value
                    if currentNode.value != value: 
                        print('Value not found in doubleLinkedList')
                        return False

                # prepare the position to insert the new node
                newNode.next = currentNode.next
                
                # set new node at the position are prepared
                currentNode.next = newNode
                
                # set pointer from prevoius of new node
                newNode.next.prev = newNode
                
                # set the new node pointer from current node
                newNode.prev = currentNode


    # remove node from the last position (tail)
    def removeNodeFromEnd(self):
        
        # check the doubleLinkedList is not empty
        if self.head != None:
            # set the initial of node
            currentNode = self.head 

            # find the tail by looping then detect the None
            while currentNode.next.next != None: 
                currentNode = currentNode.next

            # cut the chain node by set the prev and next to None
            currentNode.next.prev = None
            currentNode.next = None
            self.tail = currentNode

    # remove the node by the position (value) that want to remove
    def removeNode(self, value):

        # check the doubleLinkedList is not empty
        if self.head != None: 
            currentNode = self.head

            # the postion that want to remove is head
            if self.head.value == value: 
                
                # set the none in head value
                self.head.next.prev = None
                
                # create new head by next position
                self.head = self.head.next

            # the postion that want to remove is tail
            elif self.tail.value == value:
                
                # set the none at tail value
                self.tail.prev.next = None
                
                # set the latest before tail is new tail
                self.tail = self.tail.prev


            else:
                # check the value that want to remove is valid in doubleLinkedList
                # find the position of the node that want remove
                while currentNode.next.value != value:
                    currentNode = currentNode.next

                    # if the position (value) is invalid in doubleLinkedList
                    if currentNode.next.value != value:
                        print('Value not found in doubleLinkedList')
                        return False

                # set the next next node pointer by crossing the node that want to remove
                # the value of pointer is currentNode
                currentNode.next.next.prev = currentNode 
                
                # set the next next node to be pointer of this node
                currentNode.next = currentNode.next.next

    def display(self):
        nodeList = []

        if self.head != None:
            currentNode = self.head
            while currentNode.next != None:
                nodeList.append(currentNode.value)
                
                # move to the next node
                currentNode = currentNode.next
            
            nodeList.append(currentNode.value)
            print(nodeList)
                
        else:
            print('No nodes')
            return False



dll = DoubleLinkedList()
dll.addNode(10)
dll.display()
dll.addNode(20)
dll.display()
dll.addNode(30)
dll.display()
dll.addNode(35)
dll.display()
dll.removeNodeFromEnd()
dll.display()
dll.removeNode(20)
dll.display()
dll.insertNodeAfter(10, 90)
dll.display()

# error when not clear stack it cannot find the 90 
dll.insertNodeAfter(90, 'Pyton')
dll.display()
dll.addNode(99)
dll.display()