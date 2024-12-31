class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self) -> str:
        result = ""
        for i in range(len(self.list)-1, -1, -1):
            result += str(self.list[i])
            if i > 0:
                result += "\n"
        return result
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        return self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        
        # raw implementation:
        #
        # size = len(self.list)
        # popped_value = self.list[size-1]
        # self.list = self.list[:size-1]
        # return popped_value
        return self.list.pop()     
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.list[len(self.list)-1]
    
    def isFull(self):
        return False
    
    def delete_all(self):
        self.list = None

new_stack = Stack()
print(f"Is stack empty: {new_stack.isEmpty()}")
print(new_stack)
new_stack.push(10)
# print(new_stack)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.push(50)
print(f"Stack:\n{new_stack}\n****")      
# print("End!!")
print(new_stack.pop())
print(f"Stack:\n{new_stack}\n****")
print(new_stack.peek())
print(f"Stack:\n{new_stack}\n****")
print(f"Is stack empty: {new_stack.isEmpty()}")
print(f"Is stack full: {new_stack.isFull()}")
new_stack.delete_all()