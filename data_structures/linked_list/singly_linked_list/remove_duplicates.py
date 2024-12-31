# Remove Duplicates from a Singly Linked List
# Given a singly linked list, write a function that removes all the duplicates. use this linked list .

# Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

# Result Linked List - "1 -> 2 -> 4 -> 3"
from linked_list import LinkedList

def remove_duplicates(linked_list: LinkedList):
    # # Brute force approach: Create a new linked list and store only the unique elements in that list
    # # Time complexity: O(n), Space complexity: O(n)
    # new_linked_list = LinkedList()
    # visited = {}
    # current = linked_list.head
    # while current != None:
    #     if current.value not in visited.keys():
    #         new_linked_list.append(current.value)
    #         visited[current.value] = True
    #     current = current.next
    
    # # Optimised solution:
    if linked_list.head == None:
        return None
    unique_elements = set()
    current = linked_list.head
    unique_elements.add(current.value)
    while current.next:
        if current.next.value in unique_elements:
            next = current.next
            current.next = current.next.next
            next.next = None
        else:
            unique_elements.add(current.value)
            current = current.next
    linked_list.tail = current
    return new_linked_list

def delete_node(linked_list: LinkedList, index: int):
    print(f"Deleting node with index: {index}")
    if index == 0:
        linked_list.head = None
        linked_list.tail = None
    else:
        current = linked_list.head
        for i in range(index-1):
            current = current.next
        popped_node = current.next
        current.next = popped_node.next
        popped_node.next = None
        if index == linked_list.length - 1:
            linked_list.tail = current
    linked_list.length -= 1
    print(f"linked list post deleting index {index}: {linked_list} ")
    return linked_list

new_linked_list = LinkedList()
print(new_linked_list)
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(4)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(2)
print(new_linked_list)
print(remove_duplicates(new_linked_list))
# print(f"New linked_list: {new_linked_list}")