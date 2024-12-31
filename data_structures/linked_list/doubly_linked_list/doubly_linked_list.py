class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node:
                result += " <-> "
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    
    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
    
    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False
    
    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length-1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, new_value):
        if self.head == None:
            return
        if index < 0 or index > self.length - 1:
            return Exception("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = new_value
    
    def insert(self, index, value):
        if self.head == None:
            return
        if index < 0 or index > self.length:
            return Exception("Index out of range")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            next_node = current_node.next
            current_node.next = new_node
            next_node.prev = new_node
            new_node.prev = current_node
            new_node.next = next_node
        self.length += 1
    
    def pop_first(self):
        if self.head == None:
            return None
        popped_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.head.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
            
    def remove(self, index):
        if self.head == None:
            return
        if index < 0 or index > self.length - 1:
            return Exception("Index out of range")
        if index == 0:
            popped_node = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                popped_node.next = None
                self.head.prev = None
        elif index == self.length - 1:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            popped_node = current_node.next
            current_node.next = popped_node.next
            popped_node.next.prev = current_node
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1

new_linked_list = DLinkedList()
new_linked_list.append(4)
# print(new_linked_list)
new_linked_list.append(6)
new_linked_list.append(8)
new_linked_list.append(10)
new_linked_list.prepend(2)
print(new_linked_list)
# print(new_linked_list.search(8))
# new_linked_list.set_value(3, 11)
# print(new_linked_list.get(5))
print(new_linked_list.get(3))
# print(new_linked_list)
# print(new_linked_list.head)
# print(new_linked_list.tail)