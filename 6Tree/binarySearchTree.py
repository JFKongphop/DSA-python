# Binary Search Tree => BST
# insert the initial number
# if next number is less than is insert at leftChild
# else insert at rightChild

# DFS Preorder  | Node -> Left -> Right
# DFS Inorder   | Left -> Node -> Right
# DFS Postorder | Left -> Right -> Node

class Node(object):
    # set middle, left and right child in tree
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # insert data in the tree
    def insert(self, data):
        # BST cannot contain duplicate data
        if self.data == data:
            return False

        # data less than the root data is insert at the left of the root
        elif data < self.data:

            # if the leftChild have the data it checking again and insert it
            if self.leftChild:
                return self.leftChild.insert(data)

            # if the leftChild is empty insert the data to this position
            else:
                self.leftChild = Node(data)
                return True
        
        # data more than the root data is insert at the left of the root  
        else:
            
            # if the rightChild have the data it checking again and insert it
            if self.rightChild:
                return self.rightChild.insert(data)

            # if the rightChild is empty insert the data to this position
            else:
                self.rightChild = Node(data)
                return True
            
    # find the min value that locate at the farest of left side
    def minValueNode(self, node):
        # set initial node by parameter
        current = node

        # looping down to find the leftmost of leaf
        while current.leftChild != None:

            # moving next of leftChild
            current = current.leftChild
        
        # return the min value then found if
        return current
    
    # delete the leaf (Node) by the data
    def delete(self, data):
        
        # check the tree is empth
        if self == None:
            return None
        
        # checking the data less than or more than root and delete it
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)

        # delete the node with one child
        else:

            # leftChild is empty
            if self.leftChild == None:
                temp = self.rightChild

                # delete this node
                self = None

                # return rightChild
                return temp

            # rightChild is empty
            elif self.rightChild == None:
                temp = self.leftChild

                # delete this node
                self = None

                # return rightChild
                return temp

            # set the min value by this method at rightChild
            # because the min value is the max value of this tree
            temp = self.minValueNode(self.rightChild)

            # set the tree by rightChild
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)
        
        # return the tree then it deleted the data
        return self

    # find the data is valid or invalid
    def find(self, data):
        
        # found the data at the root
        if data == self.data:
            return True

        # the data is less than root find at leftChild
        elif data < self.data:
            
            # if leftChild is valid
            if self.leftChild:
                return self.leftChild.find(data)
            
            # not found
            return False

        # the data is more than root find at rightChild
        else:

            # if rightChild is valid
            if self.rightChild:
                return self.rightChild.find(data)
            
            # not found
            return False

    # show of all node by this algorithm
    # DFS Preorder  | Node -> Left -> Right
    # print by recursive
    def preOrder(self):

        # tree is valid
        if self:
            # response by the algorithm 
            # Node
            print(str(self.data), end = ' ')

            # Left
            if self.leftChild:
                self.leftChild.preOrder()
            
            # Right
            if self.rightChild:
                self.rightChild.preOrder()

    # show of all node by this algorithm
    # DFS Inorder  | Left -> Node -> Right
    # print by recursive
    def inOrder(self):

        # tree is valid
        if self:
            # response by the algorithm 
            # Left
            if self.leftChild:
                self.leftChild.inOrder()
            
            # Node
            print(str(self.data), end = ' ')
            
            # Right
            if self.rightChild:
                self.rightChild.inOrder()

    # show of all node by this algorithm    
    # DFS Postorder | Left -> Right -> Node
    # print by recursive
    def postOrder(self):

        # tree is valid
        if self:
            # response by the algorithm
            # Left
            if self.leftChild:
                self.leftChild.postOrder()
            
            # Right
            if self.rightChild:
                self.rightChild.postOrder()

            # Node
            print(str(self.data), end = ' ')


# create tree by the node element
class Tree(object):
    # wait it for first intial number (root)
    def __init__(self) -> None:
        self.root = None
    
    # inherit this method by Node when insert it in this tree
    def insert(self, data):

        # tree is valid (it have a root)
        if self.root:
            return self.root.insert(data)
        
        # tree is empty (root is not set)
        else:
            # set initial data (root)
            self.root = Node(data)
            return True

    # inherit this method by Node when delete it in this tree 
    def delete(self, data):

        # tree is valid (it have a root)
        if self.root:
            return self.root.delete(data)

    # inherit this method by Node when delete it in this tree 
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    # inherit this method by Node when preorder it in this tree 
    # DFS Preorder | Node -> Left -> Right 
    def preOrder(self):
        if self.root:
            print()
            print('PreOrder : ')
            self.root.preOrder()

    # inherit this method by Node when inorder it in this tree 
    # DFS Inorder | Left -> Node -> Right
    def inOrder(self):
        if self.root:
            print()
            print('InOrder : ')
            self.root.inOrder()

    # inherit this method by Node when inorder it in this tree 
    # DFS Postorder | Left -> Right -> Node
    def postOrder(self):
        if self.root:
            print()
            print('PostOrder : ')
            self.root.postOrder()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(16)
    tree.insert(18)
    tree.insert(11)
    tree.insert(10)
    tree.insert(26)
    tree.insert(14)
    tree.insert(13)
    tree.insert(21)
    tree.insert(20)
    print(tree.find(1))
    print(tree.find(26))

    ''' Following tree is getting created:
                    16
                 /      \
               11         18
              / \           \
            10   14          26
                 /          /
                13         21
                         /
                        20
    '''

    tree.preOrder()
    tree.inOrder()
    tree.postOrder()
    print('\n\nAfter deleting 26')
    tree.delete(26)
    tree.preOrder()
    tree.inOrder()
    tree.postOrder()
    print('\n\nAfter deleting 16')
    tree.delete(16)
    tree.preOrder()
    tree.inOrder()
    tree.postOrder()