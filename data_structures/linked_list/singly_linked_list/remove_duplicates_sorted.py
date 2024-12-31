# # Remove Duplicates

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

from merge_sorted_ll import print_linked_list

def add_node(head, value):
    current = head
    while current.next != None:
        current = current.next
    current.next = ListNode(val=value)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.value = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # TODO
        if head is None:
            return
        unique_set = set()
        current = head
        unique_set.add(current.val)
        while current.next:
            if current.next.val in unique_set: # duplicate element
                current.next = current.next.next
            else:
                unique_set.add(current.next.val)
                current = current.next

new_head = ListNode(1)
add_node(new_head, 1)
add_node(new_head, 2)
add_node(new_head, 2)
# add_node(new_head, 3)
print_linked_list(new_head)
Solution().deleteDuplicates(new_head)
print_linked_list(new_head)