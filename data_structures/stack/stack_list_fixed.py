class Stack:
    def __init__(self, capacity) -> None:
        self.list = []
        self.capacity = capacity
    
    def __str__(self) -> str:
        result = ""
        for index in range(len(self.list)-1, -1, -1):
            result += str(self.list[index])
            if index > 0:
                result += "\n"
        return result
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def isFull(self):
        if len(self.list) == self.capacity:
            return True
        return False
    
    def push(self, value):
        if self.isFull():
            return Exception(f"Stack is full")
        return self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.list[len(self.list)-1]
    
    def delete_all(self):
        self.list = None

new_stack = Stack(4)
print(new_stack.isEmpty())
print(new_stack.isFull())
print(f"******************")
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
print(new_stack)
print(f"******************")
print(new_stack.isFull())
new_stack.pop()
print(new_stack)
print(f"******************")
new_stack.push(50)
print(new_stack)
print(f"******************")
print(new_stack.peek())
print(f"******************")
print(new_stack)
print(f"******************")
new_stack.delete_all()
