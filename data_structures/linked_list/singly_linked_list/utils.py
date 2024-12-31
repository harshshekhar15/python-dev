class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    result = ""
    while current != None:
        result += f"{current.val} -> "
        current = current.next
    print(result)

def add_node(head, value):
    current = head
    while current.next != None:
        current = current.next
    current.next = ListNode(val=value)