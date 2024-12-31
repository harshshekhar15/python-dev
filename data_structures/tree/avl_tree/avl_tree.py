"""
AVL tree is a special kind of Binary tree in which the difference of height
of the left subtree and right subtree for any given node is not more than
1.

Create an AVL tree structure with the following methods:
- addNode : Adds a new node to the tree such that the BT is still balanced.
    Adding a new node to the tree has two conditions:
    - Tree is balanced, then don't do anything.
    - Tree is not balanced, performs rotation to balance the tree. Rotation
      is done based on the following conditions:
      - Left-left condition: Rotate the disbalanced node towards right.
      - Left-right condition: Rotate the disbalanced node's leftChild to
            left this makes the disbalanced node in left-left condition,
            then rotate right the disbalanced node.
      - Right-right condition: Rotate the disbalanced node towards left.
      - Right-left condition: Rotate the disbalanced node's right child to
            towards right this makes the disbalanced node right-right
            condition then rotate the disbalanced node towards left.
- deleteNode: Deletes a value from the tree such that the resulting BT is
    still balanced.
- preOrderTraversal: Prints the root node, left subtree and then the right
    subtree.
- inOrderTraversal: Prints the left subtree first, then the root node and
    finally the right subtree.
- postOrderTraversal: Prints the left subtree first, then the right subtree
    and finally the root node.
- levelOrderTraversal: Prints the nodes at each level one after the other.
"""

from queue_ll import QueueLL

class AVLNode:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def getHeight(rootNode):
    if rootNode == None:
        return 0
    return rootNode.height

def getBalance(rootNode):
    if rootNode == None:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def rotateRight(disbalancedNode):
    rootNode = disbalancedNode.leftChild
    disbalancedNode.leftChild = rootNode.rightChild
    rootNode.rightChild = disbalancedNode
    disbalancedNode.height = max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)) + 1
    rootNode.height = max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)) + 1
    return rootNode

def rotateLeft(disbalancedNode):
    rootNode = disbalancedNode.rightChild
    disbalancedNode.rightChild = rootNode.leftChild
    rootNode.leftChild = disbalancedNode
    disbalancedNode.height = max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)) + 1
    rootNode.height = max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)) + 1
    return rootNode

def addNode(rootNode, newValue):
    if rootNode == None:
        # rootNode = AVLNode(newValue)
        return AVLNode(newValue)
    elif newValue < rootNode.data:
        rootNode.leftChild = addNode(rootNode.leftChild, newValue)
    # elif newValue > rootNode.value:
    else:
        rootNode.rightChild = addNode(rootNode.rightChild, newValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and newValue < rootNode.leftChild.data:
        # left-left condition --> rotate right
        return rotateRight(rootNode)
    if balance > 1 and newValue > rootNode.leftChild.data:
        # left-right condition --> rotate left then right
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balance < -1 and newValue > rootNode.rightChild.data:
        # right-right condition --> rotate left
        return rotateLeft(rootNode)
    if balance < -1 and newValue < rootNode.rightChild.data:
        # right-left condition --> rotate right, then left
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode

def levelOrderTraversal(rootNode):
    if rootNode == None:
        return
    else:
        customQueue = QueueLL()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            node = customQueue.dequeue()
            print(node.value.data)
            if node.value.leftChild != None:
                customQueue.enqueue(node.value.leftChild)
            
            if node.value.rightChild != None:
                customQueue.enqueue(node.value.rightChild)

def findSmallestNode(rootNode):
    if rootNode == None or rootNode.leftChild == None:
        return rootNode
    return findSmallestNode(rootNode.leftChild)

def deleteNode(rootNode, target):
    if rootNode == None:
        return rootNode
    elif target < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, target)
    elif target > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, target)
    else:
        # Found the node to be deleted
        if rootNode.leftChild == None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild == None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # Case where both the childs are present
        successor_node = findSmallestNode(rootNode.rightChild)
        rootNode.data = successor_node.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, successor_node.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) > 0:
        return rotateRight(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) < 0:
        return rotateLeft(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode
        
        

newAVLTree = AVLNode(30)
rootNode = newAVLTree
levelOrderTraversal(rootNode)
rootNode = addNode(rootNode, 25)
rootNode = addNode(rootNode, 35)
rootNode = addNode(rootNode, 20)
rootNode = addNode(rootNode, 15)
print("***************")
levelOrderTraversal(rootNode)
rootNode = addNode(rootNode, 5)
print("***************1")
# levelOrderTraversal(rootNode)
# rootNode = addNode(rootNode, 10)
# rootNode = addNode(rootNode, 50)
# rootNode = addNode(rootNode, 60)
# rootNode = addNode(rootNode, 70)
# rootNode = addNode(rootNode, 65)
# print("*************")
levelOrderTraversal(rootNode)
rootNode = deleteNode(rootNode, 20)
print("***************2")
levelOrderTraversal(rootNode)
    