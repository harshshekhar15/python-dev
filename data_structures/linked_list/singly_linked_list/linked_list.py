class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        # print("Printing linked list:")
        temp = self.head
        linked_list = ""
        while temp != None:
            # print(temp.value)
            linked_list += str(temp.value)
            if temp.next != None:
                linked_list += " -> "
            temp = temp.next
        return linked_list

    def append(self, value):
        """
        Method to insert element at the end of linked list
        """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    
    def prepend(self, value) -> None:
        """
        Method to insert element at the start of linked list
        """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value) -> None:
        new_node = Node(value)
        temp_node = self.head
        # if the linked list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # if the index is out of range of linked list
        if index < 0 or index > self.length:
            return False
        # if we want to prepend to linked list
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        # if we want to append to linked list
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def search(self, target):
        current_node = self.head
        index = 0
        if self.head == None:
            return -1
        else:
            while current_node:
                if current_node.value == target:
                    return index 
                current_node = current_node.next
                index += 1
        return -1
    
    def get(self, index):
        current_node = self.head
        if self.head == None:
            return None
        elif index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                current_node = current_node.next
            return current_node
    
    def set_value(self, index, new_value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = new_value
            return True
        return False
    
    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        self.length -= 1
        return popped_node
    
    def pop_first(self):
        if self.head == None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if self.head == None:
            return None
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # reverse method reverses a single linked list
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head, self.tail = self.tail, self.head
    
    def middle(self):
        # case: empty linked list
        if self.head == None:
            return None
        middle = int(self.length / 2)
        current_node = self.head
        for _ in range(middle):
            current_node = current_node.next
        return current_node.value
    
    def remove_duplicates(self):
        # TODO
        if self.head == None:
            return
        unique_elements = set()
        current = self.head
        unique_elements.add(current.value)
        while current.next:
            if current.next.value in unique_elements:
                # next = current.next
                current.next = current.next.next
                # next.next = None
                self.length -= 1
            else:
                unique_elements.add(current.next.value)
                current = current.next
        self.tail = current

new_linked_list = LinkedList()
print(new_linked_list)
# new_linked_list.append(1)
# new_linked_list.append(4)
# new_linked_list.append(10)
# new_linked_list.append(15)
# new_linked_list.append(20)
print(new_linked_list)
# print(new_linked_list.remove(2))
new_linked_list.reverse()
print(new_linked_list)
print(new_linked_list.middle())