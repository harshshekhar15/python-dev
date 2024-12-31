class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        current_node = self.head
        result = ""
        while current_node != None:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += " -> "
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Index out of range")
        new_node = Node(value)
        if index == 0:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1
    
    def traverse(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def search(self, target):
        current_node = self.head
        while current_node != None:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def pop_first(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            popped_node = self.head
            self.head = self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.head == None:
            return None
        # case: only one element present in ll
        popped_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
            popped_node.next = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            # popped_node = self.tail
            current_node.next = self.head
            self.tail = current_node
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if self.head == None:
            return None
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.head == None:
            return
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0
    
    def delete_by_value(self, value):
        # Case: epmpty linked list
        if self.head == None:
            return False
        current = self.head
        if self.head == self.tail and self.head.value == value:
            self.head = self.tail = None
            current.next = None
            self.length = 0
            return True
        else:
            prev = None
            while current != None:
                if current.value == value:
                    # case: value is present at head
                    if current == self.head:
                        self.head = self.head.next
                        self.tail.next = self.head
                        current.next = None
                    else:
                        prev.next = current.next
                        current.next = None
                        # case: value is present at tail 
                        if current == self.tail:
                            self.tail = prev
                    self.length -= 1
                    return True
                prev = current
                current = current.next
        return False
    
    def split_list(self):
        # TODO
        if self.head == None:
            return None, None
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
            if current == self.head:
                break
        print(f"Length of list: {length}")
        if length % 2 == 0:
            middle = int(length / 2)
        else:
            middle = int(length / 2) + 1
        print(f"Middle node index: {middle}")
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        current = self.head
        for _ in range(0, middle):
            first_list.append(current.value)
            current = current.next
        for _ in range(middle, length):
            second_list.append(current.value)
            current = current.next

        return first_list, second_list
    
    def insert_into_sorted(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            current = self.head
            prev = None
            while current.value < data:
                prev = current
                current = current.next
                if current == self.head:
                    prev.next = new_node
                    new_node.next = self.head
                    self.tail = new_node
                    self.length += 1
                    return
            if current == self.head:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            else:
                prev.next = new_node
                new_node.next = current
            self.length += 1
        
    def josephus_circle(self, step):
        current = self.head
        prev = None
        while prev != current:
            count = 1
            while count < step:
                prev = current
                current = current.next
                count += 1
            prev.next = current.next
            current = current.next
        return current.value
                

cs_ll = CSLinkedList()
cs_ll.append(1)
cs_ll.append(2)
cs_ll.append(3)
cs_ll.append(4)
cs_ll.append(5)
cs_ll.append(6)
cs_ll.append(7)
cs_ll.append(8)
cs_ll.append(9)
print(cs_ll)
# cs_ll.insert_into_sorted(5)
# print(cs_ll)
# print(cs_ll.head.value)
print(cs_ll.josephus_circle(3))