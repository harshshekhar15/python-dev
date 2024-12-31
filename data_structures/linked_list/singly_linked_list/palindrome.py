# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

from utils import add_node, print_linked_list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.value = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        # TODO
        # new_set = set()
        # current = head
        # new_next = None
        # while current:
        #     new_node = ListNode(current.val, new_next)
        #     new_next = new_node
        #     current = current.next
        # new_head = new_next
        # print_linked_list(new_head)
        # current = head
        # while current:
        #     if current.val != new_head.val:
        #         return False
        #     current = current.next
        #     new_head = new_head.next
        # return True
        current = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            if prev.val != current.val:
                return False
            prev = prev.next
            current = current.next
        return True

new_head = ListNode(1)
add_node(new_head, 2)
# add_node(new_head, 2)
# add_node(new_head, 1)
print_linked_list(new_head)
print(Solution().isPalindrome(new_head))