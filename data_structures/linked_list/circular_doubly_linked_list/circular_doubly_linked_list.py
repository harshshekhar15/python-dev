class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)
    
class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += " <-> "
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break
    
    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False
    
    def get(self, index):
        if self.head == None:
            return None
        if index < 0 or index > self.length - 1:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node
        else:
            current_node = self.tail
            for _ in range(self.length-1, index, -1):
                current_node = current_node.prev
            return current_node
    
    def set_value(self, index, new_value):
        node = self.get(index)
        if node:
            node.value = new_value
            return True
        return False
    
    def insert(self, index, value):
        if self.head == None:
            return
        if index < 0 or index > self.length - 1:
            return
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            current_node = None
            if index < self.length // 2:
                current_node = self.head
                for _ in range(index-1):
                    current_node = current_node.next
            else:
                current_node = self.tail
                for _ in range(self.length-1, index-1, -1):
                    current_node = current_node.prev
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            self.length += 1
        
    def pop_first(self):
        if self.head == None:
            return None
        popped_node = self.head
        if self.head == self.tail:
            popped_node.next = None
            popped_node.prev = None
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        if self.head == self.tail:
            popped_node.prev = popped_node.next = None
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.prev = popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if self.head == None:
            return
        if index < 0 or index > self.length-1:
            return
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            current_node = None
            if index < self.length // 2:
                current_node = self.head
                for _ in range(index-1):
                    current_node = current_node.next
            else:
                current_node = self.tail
                for _ in range(self.length-1, index-1, -1):
                    current_node = current_node.prev
            popped_node = current_node.next
            current_node.next = popped_node.next
            popped_node.next.prev = current_node
            current_node.next = current_node.prev = None
            self.length -= 1
            return popped_node
    
    def delete_all(self):
        if self.head == None:
            return
        current_node = self.head
        while current_node:
            current_node.prev = None
            current_node = current_node.next
            if current_node == self.head:
                break
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0
            
        
        

new_cd_ll = CDLinkedList()
print(new_cd_ll)
new_cd_ll.append(10)
new_cd_ll.append(20)
new_cd_ll.append(30)
print(new_cd_ll)
new_cd_ll.prepend(5)
print(new_cd_ll)
# new_cd_ll.reverse_traverse()
# print(f"Set value: {new_cd_ll.set_value(-2, 100)}")
# new_cd_ll.insert(100, 100)
# print(new_cd_ll.remove(100))
new_cd_ll.delete_all()
print(new_cd_ll)
print(new_cd_ll.head)
print(new_cd_ll.tail)
print(new_cd_ll.length)
# print(new_cd_ll.tail)
    