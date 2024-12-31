"""
Create a queue using a linked list
"""
class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

class QueueLL:
    def __init__(self) -> None:
        self.items = LinkedList()
    
    def __str__(self) -> str:
        current_node = self.items.head
        result = ""
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node:
                result += " "
        return result
    
    def isEmpty(self):
        """
        Check if the queue is empty or not
        """
        if self.items.head == None:
            return True
        return False
    
    def enqueue(self, value):
        """
        Add a new element to the end of the queue
        """
        new_node = Node(value)
        if self.isEmpty():
            self.items.head = new_node
            self.items.tail = new_node
        else:
            self.items.tail.next = new_node
            self.items.tail = new_node
    
    def dequeue(self):
        """
        Remove the first element from the queue
        """
        if self.isEmpty():
            return None
        else:
            """
            If there are items in the queue there can be one of the
            two case:
            - There is only one item in the queue
            - There are multiple items in the queue
            """
            popped_node = self.items.head
            if self.items.head == self.items.tail:
                self.items.head = self.items.tail = None
            else:
                self.items.head = self.items.head.next
                popped_node.next = None
            return popped_node
    
    def peek(self):
        """
        Return the first element from the queue
        """
        if self.isEmpty():
            return None
        else:
            return self.items.head.value
    
    def delete(self):
        """
        Delete the entire queue
        """
        self.items.head = self.items.tail = None