class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
class StackLLFixed:
    def __init__(self, capacity) -> None:
        self.list = LinkedList()
        self.capacity = capacity
    
    def __str__(self) -> str:
        result = ""
        current_node = self.list.head
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node:
                result += "\n"
        return result
    
    def isEmpty(self):
        if self.list.head == None:
            return True
        return False
    
    def isFull(self):
        if self.list.size == self.capacity:
            return True
        return False
    
    def push(self, value):
        if self.isFull():
            return Exception("Stack is full")
        new_node = Node(value)
        # if self.isEmpty():
        #     self.list.head = new_node
        # else:
        new_node.next = self.list.head
        self.list.head = new_node
        self.list.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        popped_node = self.list.head
        self.list.head = self.list.head.next
        self.list.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.list.head.value
    
    def delete_all(self):
        self.list.head = None
        self.list.size = 0
    
new_stack = StackLLFixed(4)
print("Empty:", new_stack.isEmpty())
print("Full:", new_stack.isFull())
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
print(f"Stack:\n{new_stack}\n*****")
print(new_stack.push(50))
# print(f"Peek: {new_stack.peek()}")
# print(f"Stack:\n{new_stack}\n*****")
print(f"Pop: {new_stack.pop()}")
print(f"Stack:\n{new_stack}\n*****")
print(new_stack.push(50))
print(f"Stack:\n{new_stack}\n*****")
new_stack.delete_all()
# # print(f"Pop: {new_stack.pop()}")
# # print(f"Pop: {new_stack.pop()}")
# # print(f"Pop: {new_stack.pop()}")
print(f"Stack:\n{new_stack}\n*****")
        