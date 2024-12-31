## Merge Two Sorted Linked List

# You are given the heads of two sorted linked lists list1 and list2. 
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1: 

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3: 

# Input: list1 = [], list2 = [0]
# Output: [0]



# Constraints: 

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# from linked_list import LinkedList

# def merge_sorted_ll(ll1, ll2: LinkedList) -> LinkedList:
#     if ll1.head is None and ll2.head is None:
#         return ll1
#     elif ll1.head is None:
#         return ll2
#     elif ll2.head is None:
#         return ll1
#     result = LinkedList()
#     current_ll1 = ll1.head
#     current_ll2 = ll2.head
#     while current_ll1 != None and current_ll2 != None:
#         if current_ll1.value <= current_ll2.value:
#             result.append(current_ll1.value)
#             current_ll1 = current_ll1.next
#         else:
#             result.append(current_ll2.value)
#             current_ll2 = current_ll2.next
#     result_current = result.head
#     while result_current.next != None:
#         result_current = result_current.next
#     if current_ll1 != None:
#         result_current.next = current_ll1
#         result.tail = ll1.tail
#     elif current_ll2 != None:
#         result_current.next = current_ll2
#         result_current.tail = ll2.tail
#     return result

# linked_list1 = LinkedList()
# linked_list1.append(1)
# linked_list1.append(2)
# linked_list1.append(4)
# print(linked_list1)
# linked_list2 = LinkedList()
# linked_list2.append(1)
# linked_list2.append(3)
# linked_list2.append(4)
# print(linked_list2)
# print(f"Merged sorted linkedlist:")
# print(merge_sorted_ll(linked_list1, linked_list2))

def print_linked_list(head):
    current = head
    result = ""
    while current != None:
        result += f"{current.value} -> "
        current = current.next
    print(result)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_l1 = l1
        current_l2 = l2
        result = ListNode()
        current_result = result
        while current_l1 != None and current_l2 != None:
            if current_l1.val < current_l2.val:
                new_node = ListNode(current_l1.val)
                current_result.next = new_node
                current_result = new_node
                current_l1 = current_l1.next
            else:
                new_node = ListNode(current_l2.val)
                current_result.next = new_node
                current_result = new_node
                current_l2 = current_l2.next
        if current_l1 != None:
            current_result.next = current_l1
        if current_l2 != None:
            current_result.next = current_l2
        result = result.next
        return result