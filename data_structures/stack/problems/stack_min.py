"""
Design a Stack which has three functions - push, pop and min. min function should return the 
element with the minimum value.

Constraints:
- Push, pop and min should all operate in O(1).
"""

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Stack:
    def __init__(self) -> None:
        self.items = LinkedList()
        self.min_element = None
    
    def __str__(self) -> str:
        items = []
        current = self.items.head
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)
    
    def isEmpty(self):
        if self.items.head == None:
            return True
        return False
    
    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.items.head = self.items.tail = new_node
            self.min_element = Node(value)
        else:
            new_node.next = self.items.head
            self.items.head = new_node
            """
            Check if the pushed value is less than the current minimum or not
            
            If the inserted value is less than the current minimum then create
            a new Node and push the new value else push the current minimum
            value again in a new Node
            """
            if value < self.min_element.value:
                new_min_node = Node(value)
            else:
                new_min_node = Node(self.min_element.value)
            new_min_node.next = self.min_element
            self.min_element = new_min_node
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped_node = self.items.head
            if self.items.head == self.items.tail:
                self.items.head = self.items.tail = None
                self.min_element = None
            else:
                self.items.head = self.items.head.next
                self.min_element = self.min_element.next
            return popped_node.value         
    
    def min(self):
        return self.min_element.value
            

new_stack = Stack()
print(f"****\nStack:\n{new_stack}\n****")
new_stack.push(10)
new_stack.push(5)
new_stack.push(20)
new_stack.push(2)
print(f"****\nStack:\n{new_stack}\n****")
print(new_stack.pop())
print(f"****\nStack:\n{new_stack}\n****")
print(new_stack.min())
