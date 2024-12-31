"""
Method to insert a new node in a binary tree
"""

from queue_ll import QueueLL
from traversal import levelOrderTraversal

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.rootNode = None

    def insert(self, newNode):
        """
        insert method inserts a new node into the binary tree
        """
        if self.rootNode == None:
            self.rootNode = newNode
            return "Insertion successful"
        else:
            custom_queue = QueueLL()
            custom_queue.enqueue(self.rootNode)
            while not(custom_queue.isEmpty()):
                node = custom_queue.dequeue()
                
                if node.value.leftChild != None:
                    custom_queue.enqueue(node.value.leftChild)
                else:
                    node.value.leftChild = newNode
                    return "Insertion successful"
                
                if node.value.rightChild != None:
                    custom_queue.enqueue(node.value.rightChild)
                else:
                    node.value.rightChild = newNode
                    return "Insertion successful"
            return "Insertion failed"
        
    def search(self, target):
        """
        search method searchs a given value in the binary tree
        """
        if self.rootNode == None:
            return False
        else:
            elements_queue = QueueLL()
            elements_queue.enqueue(self.rootNode)
            while not(elements_queue.isEmpty()):
                node = elements_queue.dequeue()
                # print(node.value)
                if node.value.data == target:
                    return True
                if node.value.leftChild != None:
                    elements_queue.enqueue(node.value.leftChild)
                
                if node.value.rightChild != None:
                    elements_queue.enqueue(node.value.rightChild)
            return False
    
    def deepest_node(self):
        """
        deepest_node returns the node at the very end of the binary tree
        """
        if self.rootNode == None:
            return "Empty BT"
        else:
            custom_queue = QueueLL()
            custom_queue.enqueue(self.rootNode)
            while not(custom_queue.isEmpty()):
                node = custom_queue.dequeue()
                if node.value.leftChild != None:
                    custom_queue.enqueue(node.value.leftChild)
                
                if node.value.rightChild != None:
                    custom_queue.enqueue(node.value.rightChild)
            return node.value
    
    def delete_deepest_node(self):
        """
        delete_deepest_node deletes the node at the very end of the binary tree
        """
        if self.rootNode == None:
            return "Empty BT"
        else:
            deepestNode = self.deepest_node()
            custom_queue = QueueLL()
            custom_queue.enqueue(self.rootNode)
            while not(custom_queue.isEmpty()):
                node = custom_queue.dequeue()
                if node == deepestNode:
                    node = None
                    return "Deletion successful"
                if node.value.rightChild != None:
                    if node.value.rightChild == deepestNode:
                        node.value.rightChild = None
                        return "Deletion successful"
                    else:
                        custom_queue.enqueue(node.value.rightChild)
                if node.value.leftChild != None:
                    if node.value.leftChild == deepestNode:
                        node.value.leftChild = None
                        return "Deletion successful"
                    else:
                        custom_queue.enqueue(node.value.leftChild)
    
    def delete(self, target):
        """
        delete method will find the value to be deleted from the BT and
        will swap it with the deepest node and delete the deepest node
        """
        if self.rootNode == None:
            return "Empty BT"
        else:
            custom_queue = QueueLL()
            custom_queue.enqueue(self.rootNode)
            while not(custom_queue.isEmpty()):
                node = custom_queue.dequeue()
                if node.value.data == target:
                    deepestNode = self.deepest_node()
                    node.value.data = deepestNode.data
                    self.delete_deepest_node()
                    return "Deletion successful"
                if node.value.leftChild != None:
                    custom_queue.enqueue(node.value.leftChild)
                if node.value.rightChild != None:
                    custom_queue.enqueue(node.value.rightChild)
            return "Value not found"
                    

                        
            
        

newBT = BinaryTree()
# newNode = TreeNode(2)
# insertNodeBT(newBT, newNode)
# insertNodeBT(newBT, TreeNode(5))
levelOrderTraversal(newBT.rootNode)
newBT.insert(TreeNode(2))
levelOrderTraversal(newBT.rootNode)
print("*******")
newBT.insert(TreeNode(4))
newBT.insert(TreeNode(6))
newBT.insert(TreeNode(8))
newBT.insert(TreeNode(10))
newBT.insert(TreeNode(12))
levelOrderTraversal(newBT.rootNode)
print(f"Deepest Node: {newBT.delete(4)}")
levelOrderTraversal(newBT.rootNode)
print(newBT.search(4))