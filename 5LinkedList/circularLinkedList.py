# Circular Linked List − Last item contains link of the first element as next and the first element has a link to the last element as previous.
# can insert the item all of the position on linikedList

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

class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

class CircularLinkedList:
    def __init__(self, head = None) -> None:
        # set the head value is None
        self.head = head

    # insert the node at the last position (tail)
    def insertNodeEnd(self, key):
        # create new node
        newNode = Node(key)

        # if node is empty
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
        
        # it have the node in circular
        else:
            currentNode = self.head
            
            # find the tail of node by looping then detect the self.head
            # because it connect the head with tail by circular
            while currentNode.next != self.head:
                currentNode = currentNode.next
            
            # the detect the tail of node set it to the last
            currentNode.next = newNode

            # connect the newNode with the head
            newNode.next = self.head

    # insert node at begining of it (before the head)
    def insertNodeStart(self, key):
        newNode = Node(key)

        # if the circular is have only one element
        currentNode = self.head
        
        # set the head after the newNode (newNode => at the position newNode.next = self.head)
        newNode.next = self.head
    
        # if the node is empty doesn't have any element
        if self.head == None:
            # set it at next of new node
            newNode.next = newNode

        # it not empty insert the node at the 
        else:
            # find the head node then it detect
            while currentNode.next != self.head:
                currentNode = currentNode.next
            
            # set the currentNode (head) to be new node
            # insert the new node before of the head
            currentNode.next = newNode
        
        # set the new node at the head before the initial node
        self.head = newNode
    
    # insert by the position (node value)
    # @param keyPosition is the value of this node that find to be insert after it
    def insertAfterNode(self,  keyPosition, key):
        # set inistail node is head
        currentNode = self.head

        # find the position of value that want to insert
        while currentNode:
            
            # it have only one at the head or intial of circular
            # and this node value is equal the keyPosition
            if currentNode.next == self.head and currentNode.key == keyPosition:
                self.append(key)
                return

            # detect the key of node is detect
            elif currentNode.key == keyPosition:
                # create node
                newNode = Node(key)
                # prepare the nextNode to connect of the new node
                nextNode = currentNode.next

                # update the pointer of newNode
                # the pointer of newNode is the value of nextNode
                currentNode.next = newNode
                newNode.next = nextNode
                
                return

            # the current is head of node
            # the circular is still at the same position
            else:
                if currentNode.next == self.head:
                    break

            # if the condition is not match
            # moving to the next node
            currentNode = currentNode.next

    # deelete by the node value (key)
    def delete(self, deleteKey):
        # set the initial node to search
        currentNode = self.head
        prevNode = None

        while currentNode:

            # it like to find it the method (insertAfterNode)
            # it have only one at the head or intial of circular
            # and this node value is equal the keyPosition
            if currentNode == self.head and currentNode.key == deleteKey:
                
                # case 1
                # if the circular is only one element it circulate when find then it still the same of value at head
                if currentNode.next == self.head:
                    # clear it by the defauld by set it to be None
                    currentNode = None
                    self.head = None
                    return
                
                # case 2
                # it have multiple element in circular but delete at head
                else:
                    # find the position (key) to delete
                    while currentNode.next != self.head:
                        currentNode = currentNode.next
                
                    # set the next of node by next of head
                    currentNode.next = self.head.next
                    
                    # set this head by the next of head because will cut the current head
                    self.head = self.head.next

                    # cut it out by the None value
                    currentNode = None
                    return
            
            # case 3 - 4
            # delete of the body it between the circular (not head)
            elif currentNode.key == deleteKey:
                # set the value of current before delete to be prevNode
                prevNode.next = currentNode.next

                # cut it out by the None value
                currentNode = None
                return
            
            # the current is head of node
            # the circular is still at the same position
            else: 
                if currentNode.next == self.head:
                    break

            # set the nextNode when delete to connect the node after delete again by this value
            prevNode = currentNode

            # if the condition is not match
            # moving to the next node
            currentNode = currentNode.next        


    def display(self):
        cirList = ''
        currentNode = self.head

        while currentNode:
            cirList += '{0: 1d}'.format(currentNode.key)
            currentNode = currentNode.next
            
            if currentNode == self.head:
                break
            
        print(cirList)


cll = CircularLinkedList(None)
cll.insertNodeEnd(30)
cll.display()
cll.insertNodeEnd(90)
cll.display()
cll.insertNodeStart(60)
cll.display()
cll.insertAfterNode(60, 66)
cll.display()
cll.delete(66)
cll.display()