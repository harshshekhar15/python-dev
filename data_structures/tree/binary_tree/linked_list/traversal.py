"""
Popular methods to traverse a binary tree
"""
from queue_ll import QueueLL
        
# newBT = TreeNode("Drinks")
# left_child = TreeNode("Hot")
# right_child = TreeNode("Cold")
# newBT.leftChild = left_child
# newBT.rightChild = right_child
# left_child.leftChild = TreeNode("Tea")
# left_child.rightChild = TreeNode("Coffee")
# right_child.leftChild = TreeNode("Non-Alcoholic")
# right_child.rightChild = TreeNode("Alcoholic")


def preOrderTraversal(rootNode):
    """
    Preorder taversal method prints the root node first, then the left child and
    finally the right child.
    """
    if rootNode == None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# print("*********\npreOrderTraversal\n*********")
# preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
    """
    Inorder traversal method prints the left child first, then the root node and
    finally the right child
    """
    if rootNode == None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# print("\n*********\ninOrderTraversal\n*********")
# inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
    """
    Postorder traversal prints the left child first, then the right child and
    finally the root node
    """
    if rootNode == None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# print("\n*********\npostOrderTraversal\n*********")
# postOrderTraversal(newBT)

def levelOrderTraversal(rootNode):
    """
    Levelorder traversal prints the nodes at all the levels starting from the
    root node and then its child and then their child starting from left
    
    Here we're using a queue to add nodes and it's child and print level
    order travesal of the tree
    """
    if rootNode == None:
        return
    else:
        elements_queue = QueueLL()
        elements_queue.enqueue(rootNode)
        # print(rootNode.data)
        while not(elements_queue.isEmpty()):
            node = elements_queue.dequeue()
            print(node.value.data)
            if node.value.leftChild != None:
                elements_queue.enqueue(node.value.leftChild)
            if node.value.rightChild != None:
                elements_queue.enqueue(node.value.rightChild)


# print("\n*********\nlevelOrderTraversal\n*********")
# levelOrderTraversal(newBT)     
