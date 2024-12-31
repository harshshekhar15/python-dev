"""
Create a circular Queue with a fixed capacity using python lists
"""

class CircularQueue:
    def __init__(self, capacity) -> None:
        self.items = capacity * [None]
        self.start = -1
        self.end = -1
        self.capacity = capacity
    
    def __str__(self) -> str:
        items = [str(x) for x in self.items]
        return ' '.join(items)
    
    def isEmpty(self):
        """
        Check if the queue is empty
        """
        if self.end == -1:
            return True
        return False
    
    def isFull(self):
        """
        Check if the queue has reached it's capacity
        """
        if self.start == 0 and self.end + 1 == self.capacity:
            return True
        elif self.end + 1 == self.start:
            return True
        else:
            return False
    
    def enqueue(self, value):
        """
        Add an element to the end of the queue
        """
        if self.isFull():
            return Exception("Queue is full")
        else:
            """
            Three possibilities here:
            - Queue is empty
            - End is at the last of the list and the empty index is at the front
            - There are empty indexes after end
            """
            if self.isEmpty():
                self.end += 1
                self.start += 1
            elif self.end + 1 == self.capacity:
                self.end = 0
            else:
                self.end += 1
            self.items[self.end] = value
    
    def dequeue(self):
        """
        Remove the first element from the queue
        """
        if self.isEmpty():
            return Exception("Queue is empty")
        else:
            """
            Three possibilities here:
            - There is only one item in the queue.
            - The start is pointing at the end.
            - Start is in the middle of the queue.
            """
            popped_index = self.start
            if self.start == self.end:
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.capacity:
                self.start = 0
            else:
                self.start += 1
            popped_item = self.items[popped_index]
            self.items[popped_index] = None
            return popped_item
    
    def peek(self):
        """
        Return the first item from the queue
        """
        if self.isEmpty():
            return None
        else:
            return self.items[self.start]
    
    def delete(self):
        """
        Delete the entire queue
        """
        self.items = self.capacity * [None]
        self.start = -1
        self.end = -1

new_queue = CircularQueue(4)
print(new_queue)
print(new_queue.isEmpty())
print(new_queue.isFull())
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
print(new_queue)
# print(new_queue.dequeue())
# print(new_queue)
# print(new_queue.dequeue())
# print(new_queue)
# print(new_queue.dequeue())
# print(new_queue)
# new_queue.enqueue(50)
# print(new_queue)
# print(new_queue.dequeue())
# print(new_queue)
# print(new_queue.peek())
# print(new_queue.dequeue())
new_queue.delete()
print(new_queue)
    
