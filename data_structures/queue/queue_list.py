"""
Create a Queue class using python lists
"""

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def __str__(self) -> str:
        items = [str(x) for x in self.items]
        return ' '.join(items)
    
    def isEmpty(self):
        """
        Check if the queue is empty or not.
        
        Since we're using python list we can directly
        check if the list is an empty list or not.
        """
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        """
        Add an element to the end of the queue.
        
        Since we're using python lists we can just append
        the new item to the list
        """
        return self.items.append(value)
    
    def dequeue(self):
        """
        Remove the first item from the queue.
        
        Since we're using python lists it'll be the first
        element of the list.
        """
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """
        Return the first element in the queue.
        
        Since we're using python list it'll always be the
        item at 0th index.
        """
        if self.isEmpty():
            return None
        return self.items[0]
    
    def delete(self):
        """
        Delete the entire queue
        """
        self.items = None
    
new_queue = Queue()
print(new_queue)
print(new_queue.isEmpty())
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
print(new_queue)
print(new_queue.dequeue())
print(new_queue)
print(new_queue.peek())
print(new_queue)
new_queue.delete()
            