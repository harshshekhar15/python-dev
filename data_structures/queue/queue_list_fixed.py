"""
Create a queue using python lists with a fixed capacity
"""

class BufferedQueue:
    def __init__(self, capacity) -> None:
        """
        Create a queue with a fixed capacity using python list
        """
        self.items = []
        self.capacity = capacity
    
    def __str__(self) -> str:
        items = [str(x) for x in self.items]
        return ' '.join(items)
    
    def isEmpty(self):
        """
        Check if the queue is empty or not
        """
        if self.items == []:
            return True
        return False
    
    def isFull(self):
        """
        Check if the queue has reached it's capacity
        """
        if len(self.items) == self.capacity:
            return True
        return False
    
    def enqueue(self, value):
        """
        Insert an element to the end of the queue
        
        Constraint: Insert only if the queue hasn't reached
        it's capacity
        """
        if self.isFull():
            return Exception("Queue is full!")
        return self.items.append(value)
    
    def dequeue(self):
        """
        Remove the first element from the queue
        """
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """
        Returns the first element from the queue
        """
        if self.isEmpty():
            return None
        return self.items[0]
    
    def delete(self):
        """
        Delete the entire queue
        """
        self.items = None

new_queue = BufferedQueue(4)
print(new_queue)
print(new_queue.isEmpty())
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
print(new_queue)
print(new_queue.dequeue())
print(new_queue)
new_queue.enqueue(50)
print(new_queue)
print(new_queue.peek())
print(new_queue)
new_queue.delete


        
