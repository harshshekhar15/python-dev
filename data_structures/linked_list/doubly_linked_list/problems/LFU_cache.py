"""
LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

- LFUCache(int capacity): Initializes the object with the capacity of the data structure.
- int get(int key): Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value): Update the value of the key if present, or inserts the key if not
already present. When the cache reaches its capacity, it should invalidate and remove the least 
frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or
more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.use = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, capacity) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity
    
    # delete_node removes a node from the LL using node's pointer
    def delete_node(self, node):
        if self.head == None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
        else:
            left_node = node.prev
            right_node = node.next
            left_node.next = right_node
            right_node.prev = left_node
            node.prev = node.next = None
        self.size -= 1
    
    # push_node adds a node to the starting of the LL
    def push_node(self, node):
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    def get_least_freq_key(self):
        # current_node = self.tail
        least_freq_key = self.tail.key
        min_freq = self.tail.use
        current_node = self.tail.prev
        while current_node:
            # if the current node has a use counter less than the current minimum
            # update the minimum frequency to the current use counter's value and
            # also update the least_freq_key
            if current_node.use < min_freq:
                min_freq = current_node.use
                least_freq_key = current_node.key
            current_node = current_node.prev
        return least_freq_key
    
    # push_value creates a new node using the given key and value and adds
    # it to the beginning of the LL
    def push_value(self, key, value):
        new_node = Node(key, value)
        self.push_node(new_node)
        return new_node

class LFUCache:

    def __init__(self, capacity: int):
        # LFU cache will have two attributes:
        # elements: A doubly linked list to store the elements
        # elements_map: A map to store the key and its pointer
        self.elements = DoublyLinkedList(capacity)
        self.elements_map = {}

    def get(self, key: int) -> int:
        if key in self.elements_map:
            # If the key already exist in the cache then increment the use counter by 1
            # and remove it from the list and add it to the front. This way the least
            # recently used node will lie on the end of the LL
            new_key = self.elements_map[key]
            new_key.use += 1
            # rearrange the key's place in LL only if it's not present at head
            if new_key != self.elements.head:
                self.elements.delete_node(new_key)
                self.elements.push_node(new_key)
            return new_key.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.elements_map:
            # if key is already present then update the value of the key,
            # increment the use counter by 1 and remove it from the list
            # and add it to the front to keep the least recently used
            # towards the tail
            new_key = self.elements_map[key]
            new_key.value = value
            new_key.use += 1
            self.elements.delete_node(new_key)
            self.elements.push_node(new_key)
        else:
            if self.elements.size == self.elements.capacity:
                # if the capacity of the LL is full then find out the least frequently used
                # key and remove it from the list as well as from the map
                least_freq_key = self.elements.get_least_freq_key()
                least_freq_key_pointer = self.elements_map[least_freq_key]
                self.elements.delete_node(least_freq_key_pointer)
                self.elements_map.pop(least_freq_key)
            new_key = self.elements.push_value(key, value)
            self.elements_map[key] = new_key

                