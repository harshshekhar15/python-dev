"""
Create a Queue using linked list with a fixed capacity
"""

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

class BufferedQueueLL:
    def __init__(self, capacity) -> None:
        self.items = LinkedList()
        self.capacity = capacity
    
    def __str__(self) -> str:
        result = ""
        current_node = self.items.head
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
    
    def isFull(self):
        """
        Check if the queue has reached it's capacity
        """
        if self.items.size == self.capacity:
            return True
        return False
    
    def enqueue(self, value):
        """
        Add a new element to the end of the queue
        """
        if self.isFull():
            return Exception("Queue is full")
        else:
            """
            There can be two cases:
            - Queue is empty
            - Queue has some items
            """
            new_node = Node(value)
            if self.isEmpty():
                self.items.head = new_node
                self.items.tail = new_node
            else:
                self.items.tail.next = new_node
                self.items.tail = new_node
            self.items.size += 1
    
    def dequeue(self):
        """
        Remove the first item from the queue
        """
        if self.isEmpty():
            return None
        else:
            """
            There can be two cases:
            - Queue has only one item.
            - Queue has multiple items
            """
            popped_item = self.items.head
            if self.items.head == self.items.tail:
                self.items.head = self.items.tail = None
            else:
                self.items.head = self.items.head.next
                popped_item.next = None
            self.items.size -= 1
            return popped_item.value
    
    def peek(self):
        """
        Return the first item from the queue
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

new_queue = BufferedQueueLL(4)
print(new_queue)
print(new_queue.isEmpty())
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
print(new_queue)
print(new_queue.enqueue(50))
print(new_queue)
print(new_queue.dequeue())
print(new_queue)
print(new_queue.enqueue(50))
print(new_queue)
print(new_queue.peek())
print(new_queue)
new_queue.delete()