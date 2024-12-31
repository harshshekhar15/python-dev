"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity
    
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(f"{current.key}:{current.value}")
            current = current.next
            if current:
                result += " <-> "
        return result
    
    # push always add to the head of the LL
    def push_node(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return new_node
    
    def push_value(self, key, value):
        new_node = Node(key, value)
        return self.push_node(new_node)
    
    # pop always deletes from the tail of LL
    def pop(self):
        popped_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.size -= 1
        # return popped_node

class LRUCache:

    def __init__(self, capacity: int):
        # self.head = None
        # self.tail = None
        # self.length = 0
        # self.capacity = capacity
        self.elements = DoublyLinkedList(capacity)
        self.element_map = {}

    def get(self, key: int) -> int:
        if key in self.element_map:
            value = self.element_map[key].value
            # Remove the current items and attach its neighbours
            # and add the current item to the head of LL
            current = self.element_map[key]
            if current == self.elements.head:
                return value
            elif current == self.elements.tail:
                self.elements.pop()
                # current.prev = None
                # current.next = self.elements.head
                # self.elements.head.prev = current
                # self.elements.head = current
                self.elements.push_node(current)
                return value
            else:
                left_node = current.prev
                right_node = current.next
                left_node.next = right_node
                right_node.prev = left_node
                current.prev = None
                current.next = self.elements.head
                self.elements.head.prev = current
                self.elements.head = current
                return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.element_map:
            current = self.element_map[key]
            current.value = value
            if current == self.elements.head:
                return
            elif current == self.elements.tail:
                self.elements.pop()
                # current.prev = None
                # current.next = self.elements.head
                # self.elements.head.prev = current
                # self.elements.head = current
                self.elements.push_node(current)
            else:
                left_node = current.prev
                right_node = current.next
                left_node.next = right_node
                right_node.prev = left_node
                current.prev = None
                current.next = self.elements.head
                self.elements.head.prev = current
                self.elements.head = current
        else:
            # Check if we have reached the capacity of the LL
            # If yes, then pop the last element and remove it
            # from the map
            if self.elements.size == self.elements.capacity:
                self.element_map.pop(self.elements.tail.key)
                self.elements.pop()
            new_node = self.elements.push_value(key, value)
            self.element_map[key] = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
print(f"Elements: {lRUCache.elements}")
print(f"Elements map: {lRUCache.element_map}")
lRUCache.put(1,1)
print(f"Elements: {lRUCache.elements}")
print(f"Elements map: {lRUCache.element_map}")
lRUCache.put(2, 2)
print(f"Elements: {lRUCache.elements}")
print(f"Elements map: {lRUCache.element_map}")
lRUCache.get(1)
print(f"Elements: {lRUCache.elements}")
print(f"Elements map: {lRUCache.element_map}")
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(f"Elements: {lRUCache.elements}")
print(f"Elements map: {lRUCache.element_map}")