"""
Implement a Queue data structure using two stacks
"""

class Stack:
    def __init__(self):
        self.lists = []
    
    def __len__(self):
        return len(self.lists)
    
    def push(self, item):
        self.lists.append(item)
    
    def pop(self):
        if len(self) == 0:
            return None
        else:
            return self.lists.pop()

class QueueViaStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def enqueue(self, item):
        self.in_stack.push(item)
    
    def dequeue(self):
        if len(self.in_stack)== 0:
            return None
        else:
            while len(self.in_stack) != 0:
                self.out_stack.push(self.in_stack.pop())
            dequeued_item = self.out_stack.pop()
            while len(self.out_stack) != 0:
                self.in_stack.push(self.out_stack.pop())
            return dequeued_item

custom_queue = QueueViaStack()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
custom_queue.enqueue(4)
print(custom_queue.dequeue())