"""
Implement a binary search tree and the following functions:
- addNode: Adds a new node to the BST 
- search: Searchs for a value in BST
- delete: Deletes a given node from BST
- preOrderTraversal: Performs a preorder traversal of BST.
- inOrderTraversal: Performs an inorder traversal of BST.
- postOrderTraversal: Performs a postorder traversal of BST.
- levelOrderTraversal: Performs a levelorder traversal of BST.
"""
from queue_ll import QueueLL

class BTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def addNode(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    else:
        if value <= rootNode.data:
            if rootNode.leftChild != None:
                addNode(rootNode.leftChild, value)
            else:
                rootNode.leftChild = BTNode(value)
        else:
            if rootNode.rightChild != None:
                addNode(rootNode.rightChild, value)
            else:
                rootNode.rightChild = BTNode(value)
    return "Insert successful"

def search(rootNode, target):
    if rootNode == None:
        return False
    else:
        if rootNode.data == target:
            return True
        elif target < rootNode.data:
            if rootNode.leftChild != None:
                return search(rootNode.leftChild, target)
            else:
                return False
        else:
            if rootNode.rightChild != None:
                return search(rootNode.rightChild, target)
            else:
                return False

def minNode(rootNode):
    """
    minNode returns the minimum node in a BST
    """
    current_node = rootNode
    while current_node.leftChild != None:
        current_node = current_node.leftChild
    return current_node

def deleteNode(rootNode, target):
    if rootNode == None:
        return rootNode
    elif target < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, target)
    elif target > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, target)
    else:
        if rootNode.leftChild == None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild == None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        rightMin = minNode(rootNode.rightChild)
        rootNode.data = rightMin.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, rightMin.data)
    return rootNode
        
                
         

def preOrderTraversal(rootNode):
    """
    preOrderTraversal prints the root node first, then the left subtree and
    finally the right subtree
    """
    if rootNode == None:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    """
    inOrderTraversal prints the left subtree first, then the root node and
    finally the right subtree
    """
    if rootNode == None:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    """
    postOrderTraversal prints the left subtree first, then the right subtree
    and finally the root node
    """
    if rootNode == None:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levelOrderTraversal(rootNode):
    """
    levelOrderTraversal prints the nodes sequentially one level after
    the other
    """
    if rootNode == None:
        return
    else:
        custom_queue = QueueLL()
        custom_queue.enqueue(rootNode)
        while not(custom_queue.isEmpty()):
            node = custom_queue.dequeue()
            print(node.value.data)
            if node.value.leftChild != None:
                custom_queue.enqueue(node.value.leftChild)
            if node.value.rightChild != None:
                custom_queue.enqueue(node.value.rightChild)
    

newBT = BTNode(None)
addNode(newBT, 70)
addNode(newBT, 60)
addNode(newBT, 80)
addNode(newBT, 90)
addNode(newBT, 50)
addNode(newBT, 65)
addNode(newBT, 75)
addNode(newBT, 45)
addNode(newBT, 55)
levelOrderTraversal(newBT)
print(f"\n**Deleting Node**\n")
deleteNode(newBT, 500)
levelOrderTraversal(newBT)