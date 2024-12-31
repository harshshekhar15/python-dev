"""
This module contains a binary tree class implemented using python lists
of a fixed size and it's relevant methods
"""

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.capacity = size
    
    def insert(self, value):
        """
        insert method inserts a new node into the binary tree
        """
        if self.lastUsedIndex + 1 == self.capacity:
            return "Tree is full"
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
        
    def search(self, target):
        """
        search method finds the given target value into the binary
        tree and return true if found else returns false
        """
        for index in range(self.capacity):
            if self.customList[index] == target:
                return True
        return False
    
    def delete(self, target):
        if self.lastUsedIndex == 0:
            return "Empty BT"
        for index in range(1, self.lastUsedIndex+1):
            if self.customList[index] == target:
                self.customList[index] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Deletion successful"
        return "Element not found"
    
    def deleteAll(self):
        self.customList = None
        return "Deletion successful"
    
    def preOrderTraversal(self, index):
        """
        preOrderTraversal method performs a Preorder traversal of a binary tree
        
        It prints the root node first, then the left subtree and finally the
        right subtree
        """
        if index > self.lastUsedIndex:
            return
        
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
    
    def inOrderTraversal(self, index):
        """
        inOrderTraversal method performs an InOrder traversal of the binary tree
        
        It prints the left subtree first, then the root node and finally the
        right subtree
        """
        if index > self.lastUsedIndex:
            return
        
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)
    
    def postOrderTraversal(self, index):
        """
        postOrderTraversal performs a PostOrder traversal of binary tree
        
        It prints the left subtree first, then the right subtree and
        finally the root node
        """
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])
    
    def levelOrderTraversal(self):
        """
        levelOrderTraversal performs a Levelorder traversal of binary tree
        
        By defaul the elements of the binary tree are stored in the list
        in  level order only. So we will just traverse the list and print
        the elements
        """
        for index in range(1, self.lastUsedIndex+1):
            print(self.customList[index])

newBT = BinaryTree(8)
newBT.insert(2)
newBT.insert(4)
newBT.insert(6)
newBT.insert(8)
newBT.insert(10)
newBT.insert(12)
# print(f"******\nPreorder traversal\n******")
# newBT.preOrderTraversal(1)
# print(f"******\nInorder traversal\n******")
# newBT.inOrderTraversal(1)
# print(f"******\nPostorder traversal\n******")
# newBT.postOrderTraversal(1)
print(f"******\nLevelorder traversal\n******")
newBT.levelOrderTraversal()
print(newBT.deleteAll())
# print(f"******\nLevelorder traversal\n******")
# newBT.levelOrderTraversal()